from datetime import datetime
from telegram import ParseMode
from calcular_siguiente_asamblea import next_activity_from_date, Activity, get_activites_of_a_month
from settings import logger


def ajuda(update, context):
    msg = 'Lista de comandos disponibles:\n\n'
    msg += "\n".join('/' + k + ': ' + v.description for k, v in COMMANDS.items())
    logger.info("ajuda command requested")
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

    today = datetime.now()
    # loop to get the next 3 months activites on an array of activities
    msg = ""
    for i in range(3):
        next_month = today.month + i
        next_month_activities = get_activites_of_a_month(today.year, next_month)
        # loop to get the activities on the array of activities
        for activity in next_month_activities:
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
}
