from telegram.ext import CommandHandler
from telegram import InlineKeyboardMarkup
from bot import AUTHORIZED_CHATS, dispatcher
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage, sendMarkup
from bot.helper.telegram_helper import button_builder
from bot.helper.parser import get_gp_link


def scrape_gp(update, context):
    buttons = button_builder.ButtonMaker()
    buttons.buildbutton("𝗣𝗿𝗶𝗺𝗲 𝗕𝗼𝘁𝘀", "https://t.me/prime_Botz")
    buttons.buildbutton("𝗝𝗼𝗶𝗻", "https://t.me/PrimexCloud")
    reply_markup = InlineKeyboardMarkup(buttons.build_menu(1))
    try:
       query = update.message.text.split()[1]
    except:
       sendMarkup('<b>send a GPLinks along with this command 👀\n\n ❗️reply to the link wont wokrs❗️</b>\n👉🏻 command GpLink', context.bot, update, reply_markup)
       return
 
    if not query.startswith("https://gplinks") or query.startswith("gplinks"):
       sendMessage('<b>Sorry 🤐 , <i>scrape only for GPLinks. \nMore Links Bypasser Adding Soon.</i> 🤠</b>', context.bot, update)
       return

    m = sendMessage('𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗚𝗽𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸 \n𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 𝙖 𝙢𝙞𝙣𝙪𝙩𝙚.', context.bot, update)
    link = get_gp_link(query)
    deleteMessage(context.bot, m)
    if not link:      
       sendMessage("𝗦𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴 𝘄𝗲𝗻𝘁 𝘄𝗿𝗼𝗻𝗴\n𝗧𝗿𝘆 𝗮𝗴𝗮𝗶𝗻 𝗹𝗮𝘁𝗲𝗿..🥺  ", context.bot, update)
    else:
       sendMessage(f'𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗕𝘆𝗽𝗮𝘀𝘀𝗲𝗱 ✅ \n\n𝗕𝘆𝗽𝗮𝘀𝘀𝗲𝗱 𝗟𝗶𝗻𝗸: <code>{link}</code>', context.bot, update)

gplink_handler = CommandHandler("scrape", scrape_gp,
                               filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(gplink_handler)
