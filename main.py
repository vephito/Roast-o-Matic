from telegram.ext import *
from telegram import Update
import keys
import requests
import os
import openai
print('Starting up bot...')
openai.api_key=keys.openai_key



def image(word):
    image_res = openai.Image.create(
        prompt=word,
        n=1,
        size="512x512"
    )
    print(image_res['data'][0]['url'])
    return image_res['data'][0]['url']
def fetch_and_display_api(word):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Welcome to the Roast-o-Matic app, where laughter and good-natured teasing collide! Brace yourself for a hilarious experience as we whip up some delightful roasts just for you. Remember, it's all in good fun, so let's embark on a rib-tickling adventure together! "},
            {"role": "user", "content": f"{word}"},
            # {"role": "system", "content": "Oh, it seems you've entered the fun zone! Prepare yourself for some playful "
            #                              "banter and a sprinkle of humor. Don't worry, it's all in good fun! Let's "
            #                              "dive in and embrace the laughter together!"},
            #
            # {"role": "user", "content": f"{word}"},
    ]
    )

    print(completion.choices[0].message)
    return completion.choices[0].message['content']

# Example usage:



async def start_command(update, context):
    await update.message.reply_text('Hello there! i\'m Roast-o-Matic. Nice to mee you!')


async def help_command(update, context):
    await update.message.reply_text("Try typing anything and I will response!")


async def handle_messages(update, context):
    text = update.message.text
    definition = fetch_and_display_api(text)
    #await update.message.reply_photo(photo=definition, caption="This is an image!")
    await update.message.reply_text(definition)



def error(update, context):
    print(f'update {update} caused error: {context.error}')


if __name__ == '__main__':
    app = ApplicationBuilder().token(keys.token).build()


    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(None, handle_messages))



    # Errors
    app.add_error_handler(error)

    # Run bot
    app.run_polling()
    #app.run_polling(1.0)
    #app.idle()

