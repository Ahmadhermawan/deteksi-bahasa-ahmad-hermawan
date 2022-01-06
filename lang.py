from langdetect import detect

all_language_codes ={
    "en": "English",
    "ar": "Arabic",
    "de": "Deutsch",
    "id": "Bahasa Indonesia",
    "fr": "français"
}

input_sentences = [
    "I'm going on vacation this month",
    "انا ذاهب في اجازة هذا الشهر",
    "Ich fahre diesen Monat in den Urlaub",
    "Saya akan liburan bulan ini",
    "je pars en vacances ce mois ci"
]

lemmatizer_names = ["Language Code","Input Sentences"]
format_text = '{:24}' *(len(lemmatizer_names)+ 1)
print ("\n", format_text.format("Language Name", *lemmatizer_names), '\n' '='*0)
for data in input_sentences:
    language_code = detect(data)
    sentence = [all_language_codes.get(language_code), language_code, data]
    print (format_text.format(*sentence))