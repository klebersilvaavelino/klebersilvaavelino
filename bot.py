from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Substitua 'YOUR_TOKEN_HERE' pelo token do seu bot
TOKEN = '7440623841:AAGi-f84lsTIdARtAe6VR2x5jNU2eKH8Ul0'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá! Eu sou o seu bot!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Você disse: {update.message.text}')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Responde a mensagens de texto

    print("Bot está rodando...")
    app.run_polling()
