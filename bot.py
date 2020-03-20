import telebot
import requests


URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20200111T163758Z.c2902bb87052f356.b154c54dee4bc65e0c35b84a38c3d046e5368534"
TOKEN = "1032944998:AAEbvmvSYW53k8rNQBgSxvOwozWloqZ5rfE"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.forward_message(chat_id=-391611419,
                        from_chat_id=message.chat.id,
                        message_id=message.message_id)
    bot.send_message(message.chat.id,
                     '''
Привет! Вот какие языки я перевожу:
ru - Русский язык
de - Немецкий язык
uk - Украинский язык
es - Испанский язык
uz - Узбекский язык
hi - Хинди
ja - Японский язык
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
/help - полный список поддерживаемых языков
--------------------------------------------------
Как мне отправить сообщение:
--------------------------------------------------
ru-en Привет.

Написав так, бот переведет "Привет" с русского языка на английский язык. 

На заметку: Между ЯЗЫКОМ, с которого надо перевести, ЯЗЫКОМ, на который нужно перевести и ТЕКСТОМ, который нужно первесити, может стоять любой знак. Главное один!!!
                    ''')


@bot.message_handler(commands=['help'])
def help(message):
    bot.forward_message(chat_id=-391611419,
                        from_chat_id=message.chat.id,
                        message_id=message.message_id)
    bot.send_message(message.chat.id,
                     '''
Вот какие языки я перевожу:
ru - Русский язык
de - Немецкий язык
uk - Украинский язык
es - Испанский язык
uz - Узбекский язык
hi - Хинди
ja - Японский язык
az - Азербайджанский язык
ar - Арабский язык
hy - Армянский язык
af - Африкаанс
ba - Башкирский язык
be - Белорусский язык
vi - Вьетнамский язык
nl - Голландский язык
el - Греческий язык
ka - Грузинский язык
ga - Ирландский язык
it - Италбянский язык
is - Исландский язык
kk - Казахский язык
kn - Каннада
ky - Киргизский язык 
ko - Корейский язык
zh - Китайский язык
la - Латынь
mk - Македонский язык
mn - Монгольский язык
pt - Португальский язык
sr - Сербский язык
tg - Таджикский язык
tt - Татарский язык
tr - Турейский язык
fr - Француский язык
gd - Шотландский язык
et - Эстонский язык
                     ''')


@bot.message_handler(content_types=['text'])
def translator(message):
    bot.forward_message(chat_id=-391611419,
                        from_chat_id=message.chat.id,
                        message_id=message.message_id)
    words = message.text[6:]
    lang = (message.text[:2] + '-' + message.text[3:5]).lower()

    def translate():
        params = {
            'key': KEY,
            'text': words,
            'lang': lang
        }
        response = requests.get(URL, params=params)
        return response.json()

    json = translate()
    try:
        bot.send_message(message.chat.id, json['text'])
    except KeyError:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIEil5nunwQRp5W_OHL6M3FiSs1ZnHHAAJMAAN130EDkskvMY2LmRkYBA')
        bot.send_message(message.chat.id, 'ERROR \nЧто-то пошло не так. Проверь свой запрос и исправь ошибку)')


bot.polling(none_stop=True, interval=0)
