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

MISSATGE_BENVINGUDA="""
Hola!

Gràcies per l'interès en el nostre projecte. Abans de res volem deixar clar que això no és un gimnàs ordinari, som un centre social okupat i autogestionat, les activitats que es fan són gratuïtes, però la participació en l'espai en una o altra activitat implica també la responsabilitat de participar en les assemblees, del projecte del gim quinzenalment, els torns de neteja i jornades de treball periòdicament. Això és important, així que us preguem que valoreu si us podreu comprometre, volem evitar la lògica de usuari i consum de l'espai, que estem acostumades a viure en el sistema capitalista.

Sobretot som un espai polític per la qual cosa venir a entrenar implica participar en l'activitat política i de gestió de l'espai.

Aquí (https://lacinetika.wordpress.com/gimnas/) pots veure totes les activitats regulars que hi ha ara mateix, però demanem a les persones noves que vulguin venir a entrenar que vinguin a una assemblea abans per poder-se presentar i donar-les la benvinguda i explicar com funciona bé l'espai.

Per això, abans de poder unir-te al grup d'entrenament hauries de passar  per l'assemblea del gimnàs per presentar-te i que parlem de com funciona el projecte.

Aquí unes octavetes que expliquen el projecte 🙂

https://lacinetika.files.wordpress.com/2023/10/octavila-castellano.pdf
"""