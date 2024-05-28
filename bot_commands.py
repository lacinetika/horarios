from datetime import datetime
from telegram import ParseMode
from calcular_siguiente_asamblea import next_activity_from_date, Activity, get_activites_of_a_month, properes_numero
from settings import logger, PROPERES_COUNT, MISSATGE_BENVINGUDA


def missatge_de_benvinguda(update):
    update.message.reply_text(MISSATGE_BENVINGUDA, disable_web_page_preview=True)


def ajuda(update, context):
    logger.info("ajuda command requested")
    missatge_de_benvinguda(update)
    msg = 'Llista de comandes disponibles:\n\n'
    msg += "\n".join('/' + k + ': ' + v.description for k, v in COMMANDS.items())
    update.message.reply_text(msg)


def proxima(update, context):
    logger.info("proxima command requested")
    next_activity: Activity = next_activity_from_date(datetime.now())
    update.message.reply_text(next_activity.telegram_repr, parse_mode=ParseMode.MARKDOWN)


def properes(update, context):
    """
    function that send returna bot message with the next activities on the following 3 months using the get_activites_of_a_month function.
    It return the date on the following format:
    Day name, day number of the month, month name, the hours and the name of the activity
    :param bot:
    :param update:
    :return:
    """
    logger.info("properes command requested")
    msg = ""
    for activity in properes_numero(PROPERES_COUNT):
        # format the message
        msg += "🌟" + activity.telegram_repr + "\n"
        # send the message
    update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)


class Command(object):
    def __init__(self, function, description: str, args=False):
        self.function = function
        self.args = args
        self.description = description


COMMANDS = {
    'ajuda': Command(ajuda, args=False, description='Mostra l\'ajuda'),
    'proxima': Command(proxima, args=False, description='En quin horari es la pròxima assemblea?'),
    'properes': Command(properes, args=False, description='Horaris de les properes (poden estar subjectes a canvis, mirar regularment)'),
    'start': Command(ajuda, args=False, description='Mostra l\'ajuda'),
}

