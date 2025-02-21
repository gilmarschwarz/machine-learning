#!pip install gTTS

from gtts import gTTS
from IPython.display import Audio

#English
text_to_say = "How are you doing?."
language = "en"
gtts_object = gTTS(text = text_to_say,
                  lang = language,
                  slow = False)
gtts_object.save("/content/english.wav")

#French
french_text = "Je vais au supermarché"
french_language = "fr"
french_gtts_object = gTTS(text = french_text,
                          lang = french_language,
                          slow = True)
french_gtts_object.save("/content/french.wav")

#Portuguese
port_text = "Olá, tudo bem?"
port_language = "pt"
port_gtts_object = gTTS(text = port_text,
                        lang = port_language,
                        slow = False)
port_gtts_object.save("/content/portuguese.wav")

Audio("/content/portuguese.wav")
#Audio("/content/french.wav")
#Audio("/content/english.wav")
