from translate import Translator

translator= Translator(from_lang="english",to_lang="hindi")
text = translator.translate("Good Morning!")
print(text)

