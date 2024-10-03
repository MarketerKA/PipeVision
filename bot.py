import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.utils.i18n import I18n
from video_processor import process_video  # Import the video processing function

# Initialize bot with token
API_TOKEN = '8004770304:AAFDFmQW5Dla-jQ-LJ-2Ws5mxrFIdXWTZmk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Send me a video and I'll process it with filters!")

@router.message(F.content_type == "video")
async def handle_video(message: types.Message):
    await message.reply("Processing your video...")

    video = message.video
    file_info = await bot.get_file(video.file_id)
    video_path = f"{video.file_unique_id}.mp4"
    await bot.download_file(file_info.file_path, destination=video_path)

    output_video_path = f"processed_{video.file_unique_id}.mp4"
    process_video(video_path, output_video_path)

    video_to_send = FSInputFile(output_video_path)
    await message.answer_video(video=video_to_send)

    os.remove(video_path)
    os.remove(output_video_path)

@router.message(F.content_type.in_({'text', 'photo', 'document', 'audio'}))
async def unsupported_message(message: types.Message):
    await message.reply("Please send me a video to process!")

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
