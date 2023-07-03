from telegram.ext import *
from telegram import Update
import keys
import requests
print('Starting up bot...')


def fetch_and_display_api(word):
    #response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/association/"

    querystring = {"entry": "mask"}

    headers = {
        "X-RapidAPI-Key": "5f96d16109msh06981ac9da7d47fp19802fjsn9c7d60796906",
        "X-RapidAPI-Host": "twinword-word-graph-dictionary.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


# Example usage:



async def start_command(update, context):
    fetch_and_display_api()
    await update.message.reply_text('Hello there! i\'m a bot. Nice to mee you!')


async def help_command(update, context):
    await update.message.reply_text("Try typing anything and I will response!")


async def custom_command(update, context):
    await update.message.reply_text(f"This is a custom command!")

async def handle_messages(update, context):
    text = update.message.text
    definition = fetch_and_display_api(text)
    await update.message.reply_text(definition)



def error(update, context):
    print(f'update {update} caused error: {context.error}')


if __name__ == '__main__':
    app = ApplicationBuilder().token(keys.token).build()


    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(MessageHandler(None, handle_messages))



    # Errors
    app.add_error_handler(error)

    # Run bot
    app.run_polling()
    #app.run_polling(1.0)
    #app.idle()

