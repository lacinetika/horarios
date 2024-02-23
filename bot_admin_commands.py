from datetime import datetime
from telegram import ParseMode

from bot_commands import Command
from calcular_siguiente_asamblea import next_activity_from_date, Activity, get_activites_of_a_month, properes_numero
from settings import logger, PROPERES_COUNT, MISSATGE_BENVINGUDA, START_DATE, COUNT_FROM


def admin(update, context):
    logger.info("admin command requested")
    msg = 'Llista de comandes disponibles:\n\n'
    msg += "\n".join('/' + k + ': ' + v.description for k, v in ADMIN_COMMANDS.items())
    update.message.reply_text(msg)


def settings(update, context):
    logger.info("settings command requested")
    msg = f"START_DATE: {START_DATE}\n"
    msg += f"COUNT_FROM: {COUNT_FROM}"
    update.message.reply_text(msg)


def teststart(update, context):
    try:
        logger.info("teststart command requested" + str(context.args))
        arg = context.args[0]
        msg = ""
        start_date = datetime.strptime(arg, '%Y-%m-%d')
        for activity in properes_numero(PROPERES_COUNT, start_date):
            # format the message
            msg += "🌟" + activity.telegram_repr + "\n"
        update.message.reply_text(msg)
    except Exception as e:
        update.message.reply_text(f"Error {e}")


ADMIN_COMMANDS = {
    'admin': Command(admin, args=False, description='Show admin commands'),
    'settings': Command(settings, args=False, description='Get actual settings'),
    'teststart': Command(teststart, args=True, description='Test proximes a partir de una data format YYYY-MM-DD'),
    'setstart': Command(admin, args=False, description='Set the start date'),
}
