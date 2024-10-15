import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8034345445:AAFm7X_v5EEWPm-1XlIVnyc-ss2xqZ-XaeU"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Welcome to the bot!")


async def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()


def run():
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e) == "This event loop is already running":
            # Fetch the running loop and create a new task for main
            loop = asyncio.get_event_loop()
            loop.create_task(main())
        else:
            raise


if __name__ == "__main__":
    # Make sure to import nest_asyncio and apply it
    try:
        import nest_asyncio

        nest_asyncio.apply()
    except ImportError:
        print("You can install nest_asyncio with: pip install nest_asyncio")

    run()
