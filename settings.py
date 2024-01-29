import locale
import logging

START_DATE = "2023-11-14"
SCHEDULES = '''
{
    "monday": { "18:00": "💥Thai", "20:30": "🥊Box" },
    "tuesday": { "18:00": "🥋Ninjutsu", "19:30": "💥Thai" },
    "wednesday": { "18:00": "💥Thai", "20:30": "🥊Box" },
    "thursday": { "18:00": "🥋Ninjutsu", "19:30": "💥Thai" },
    "friday": { "17:30": "🏋️‍♂️Entrenament Lliure" }
}
'''

PROPERES_COUNT=10 # Number of next classes to show

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# locale.setlocale(locale.LC_TIME, 'de_DE')