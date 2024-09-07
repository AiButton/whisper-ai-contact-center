from gtts import gTTS
from pydub import AudioSegment
import os

# English part
tts_en = gTTS("The two lakes of Bhopal still dominate the city, and are indeed its nucleus. Bordered along their shores stand silent sentinels that testify to the growth of the city. Bhopal today presents a multi-faceted profile; the old city with its marketplaces and fine old mosques and palaces still bears the aristocratic imprint of its former rulers, among them the succession of powerful Begums who ruled Bhopal from 1819 to 1926. Equally impressive is the new city with its verdant, exquisitely laid out parks and gardens, broad avenues and streamlined modern edifices. It is greener and cleaner than most cities in the country.?", lang='en')
tts_en.save("english.mp3")

# French part
tts_fr = gTTS("""Véronique Besse est députée de la Vendée (divers droite), ancienne vice-présidente du Conseil Général de la Vendée en charge des affaires sociales.""", lang='fr')
tts_fr.save("french.mp3")

# Combine audio files
english = AudioSegment.from_mp3("english.mp3")
french = AudioSegment.from_mp3("french.mp3")
combined = english + french
combined.export("multilingual.mp3", format="mp3")

# Clean up
os.remove("english.mp3")
os.remove("french.mp3")

