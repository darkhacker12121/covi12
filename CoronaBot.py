from telethon import TelegramClient, events
import json
import requests

APP_ID=123456 #my.telegram.org
APP_HASH='9c0b22d8heh3ruhr473903a079acde6ee2' #my.telegram.org
BOTT='11923432997:AAExV-jcyU9qL_j3eji3BmTDrTs2ky1T0'#@botfather

bot = TelegramClient('bot', APP_ID, APP_HASH).start(bot_token=BOTT)

def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "https://img.imageupload.net/2020/10/14/photo_2020-10-14_23-08-10.jpg",
    "caption": "**ශ්‍රී ලංකාවේ කොරෝනා තතු එසැනින් දැනගන්න.** @  **මෙම බොට්ව ඔබගේ සමුහයට Add කරගැනිමෙන් පසු ස්වයංක්‍රියව නවතම කොරෝනා තතු ලබාගත හැක. වැඩි දූර විස්තර සදහා @kavinduaj සම්බන්ධ කරගන්න.** ",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": "✅ සමුහයට ඒකතු කරන්න.",
                    "url": "https://t.me/coronasrilankabot?startgroup=new"
                }
            ]
        ]
    }
}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)

def staa():
    r = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
    jsondata = json.loads(r.text)
    update_date_time    = str(jsondata['data']['update_date_time'])
    local_new_cases     = str(jsondata['data']['local_new_cases'])
    local_active_cases  = str(jsondata['data']['local_active_cases'])
    local_total_cases   = str(jsondata['data']['local_total_cases'])
    local_deaths        = str(jsondata['data']['local_deaths'])
    local_recovered     = str(jsondata['data']['local_recovered'])
    local_total_number_of_individuals_in_hospitals = str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
    global_new_cases    = str(jsondata['data']['global_new_cases'])
    global_total_cases  = str(jsondata['data']['global_total_cases'])
    global_deaths       = str(jsondata['data']['global_deaths'])
    global_new_deaths   = str(jsondata['data']['global_deaths'])
    global_recovered    = str(jsondata['data']['global_recovered'])

    textt = str(
                    '<b>දැනට පවතින තත්වය</b>' + '\n' + '\n' + '<u>' +
                    update_date_time + ' *වන විට*</u>' + '\n' + '\n' +
                    '<u><b>🇱🇰ශ්‍රී ලංකාවේ තත්ත්වය</b></u>' + '\n' + '\n' +
                    '<b>♻️තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) =</b> ' +
                    local_total_cases + '\n' +
                    '<b>♻️ප්‍රතිකාර ලබන රෝගීන් සංඛ්‍යාව =</b> ' + local_active_cases +
                    '\n' + '<b>♻️නව රෝගීන් සංඛ්‍යාව =</b>' + local_new_cases +
                    '\n' +
                    '<b>♻️දැනට රෝහල්වල විමර්ශන යටතේ සිටින පුද්ගලයින්</b> = ' +
                    local_total_number_of_individuals_in_hospitals + '\n' +
                    '<b>♻️සුවය ලබා පිටව ගිය සංඛ්‍යාව = </b>' + local_recovered +
                    '\n' + '♻️*මරණ සංඛ්‍යාව* = ' + local_deaths + '\n' +
                    '\n' + '<u><b>🌍ලොව පුරා තත්ත්වය<b></u>' + '\n' +
                    '\n' + '<b>♻️තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) =</b>' +
                    global_total_cases + '\n' + '<b>♻️නව රෝගීන් සංඛ්‍යාව = </b>' +
                    global_new_cases + '\n' + '<b>♻️මරණ සංඛ්‍යාව =</b> ' +
                    global_deaths + '\n' + '<b>♻️සුවය ලැබූ සංඛ්‍යාව =</b>' +
                    global_recovered + '\n' + '\n' + '\n' +
                    '<b>💁‍♂️සියලු තොරතුරු රජයේ සහ පිලිගත් මුලාශ්‍ර මගිනි*🔖</b>' + '\n' +
                    '@')
    return textt



@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    staat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/corona'))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond('කොරොනා අලුත් තතු ලබා ගැනිමට පහත විදානය භාවිතා කරන්න 👉 /corona')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
