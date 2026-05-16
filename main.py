import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8943213053:AAH2FczKeS2jSHzfNKk-InOQaLCDcieYI5I"

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Salom")
@dp.message(Command("verify"))
async def command_verify_handler(message: Message) -> None:
    await message.answer("Tekshirilmoqda...")
@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer("Qanday yordam kerak?")
    @dp.message()
    async def all_message_handler(message: Message):
        await message.answer("Iltimos, komandalarni ishlating: /start, /verify, /help")
# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
          