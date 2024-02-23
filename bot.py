from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot_admin_commands import ADMIN_COMMANDS
from bot_commands import COMMANDS
from secrets import BOT_TOKEN


# def check_admin_middleware(bot, update):
#     if update and update.message and update.message.text and update.message.text.replace('/', '') in ADMIN_COMMANDS.keys():
#         if update.effective_user and update.effective_user.username in SETTINGS['ADMIN_LIST'] or \
#                 update.effective_user.id in SETTINGS['ADMIN_LIST']:
#             constants.warning_log.warning("Admin user connected : " + str(update.effective_user))
#         else:
#             constants.warning_log.warning("Attempt to access admin commands " + str(update.effective_user))
#             for msg in SETTINGS['BANNED_MESSAGE']: bot.send_message(update.effective_chat.id, msg, )
#             raise DispatcherHandlerStop


# Define command handlers. These usually take the two arguments update and context.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am your bot.')

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def start_bot():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    for k, v in {**COMMANDS, **ADMIN_COMMANDS}.items():
        chandler = CommandHandler(k, v.function, pass_args=v.args)
        updater.dispatcher.add_handler(chandler, group=1)

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

