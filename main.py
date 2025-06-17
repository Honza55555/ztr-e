from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
import os

TOKEN = os.getenv("BOT_TOKEN")

texts = {
    "cz_menu": "🥐 COFFEE PERK MENU ☕️\n\nU nás nejde jen o kafe. Je to malý rituál. Je to nálada. Je to... láska v šálku. 💘\n\n"
               "☕ Výběrová káva\n🍳 Snídaně (lehké i pořádné)\n🍰 Domácí dorty\n🥗 Brunch a saláty\n\n"
               "📄 Kompletní menu:\n👉 https://www.coffeeperk.cz/jidelni-listek\n\n"
               "Ať už si dáte espresso, matchu nebo zázvorovku – tady to chutná líp. 💛",
    "cz_hours": "🕐 KDY MÁME OTEVŘENO?\n\n"
                "📅 Pondělí–Pátek: 7:30 – 17:00\n"
                "📅 Sobota & Neděle: ZAVŘENO\n\n"
                "Chcete nás navštívit? Jsme tu každý všední den od brzkého rána.\n"
                "Těšíme se na vás! ☕",
    "cz_location": "📍 KDE NÁS NAJDETE?\n\n"
                   "🏠 Vyskočilova 1100/2, Praha 4\n"
                   "🗺️ Mapa: https://goo.gl/maps/XU3nYKDcCmC2\n\n"
                   "Stylová kavárna, příjemná atmosféra a lidi, co kávu berou vážně i s úsměvem. Zastavte se.",
    "cz_contact": "📞 KONTAKTUJTE NÁS\n\n"
                  "📬 E-mail: info@coffeeperk.cz\n"
                  "📞 Telefon: +420 725 422 518\n\n"
                  "Rádi vám pomůžeme s rezervací nebo dotazy. Jsme tu pro vás.",
    "cz_preorder": "📦 PŘEDOBJEDNÁVKY\n\n"
                   "Brzy spustíme možnost objednat si kávu a snídani předem přes Telegram. "
                   "Zatím nás navštivte osobně – těšíme se! ☕️",
    "cz_reasons": "😎 DŮVODY, PROČ SI ZAJÍT NA KÁVU\n\n"
                  "☕ Protože svět se lépe řeší s kofeinem.\n"
                  "📚 Práce počká – espresso ne.\n"
                  "💬 Dobrá konverzace začíná u šálku.\n"
                  "👀 Dnes jste už skoro byli produktivní.\n"
                  "🧠 Mozek startuje až po druhé kávě.\n"
                  "🌦️ Venku prší… nebo svítí slunce… nebo prostě cítíte, že je čas.\n\n"
                  "A někdy netřeba důvod. Prostě jen přijďte. 💛"
}

def start(update: Update, context: CallbackContext):
    kb = [
        [InlineKeyboardButton("🇨🇿 Čeština", callback_data='lang_cz')],
        [InlineKeyboardButton("🌍 English",  callback_data='lang_en')],
    ]
    update.message.reply_text(
        "☕️ Vítejte v Coffee Perk!\nTěší nás, že jste tu. 🌟\nProsím, vyberte si jazyk. 🗣️\n\n"
        "☕️ Welcome to Coffee Perk!\nWe’re happy to see you here. 🌟\nPlease choose your language. 🗣️",
        reply_markup=InlineKeyboardMarkup(kb)
    )

def language_selected(update: Update, context: CallbackContext):
    q = update.callback_query
    q.answer()
    if q.data == 'lang_cz':
        kb = [
            [InlineKeyboardButton("🧾 Menu a nabídka", callback_data='cz_menu')],
            [InlineKeyboardButton("🕐 Otevírací doba", callback_data='cz_hours')],
            [InlineKeyboardButton("📍 Kde nás najdete", callback_data='cz_location')],
            [InlineKeyboardButton("📞 Kontakt / Rezervace", callback_data='cz_contact')],
            [InlineKeyboardButton("📦 Předobjednávka (již brzy)", callback_data='cz_preorder')],
            [InlineKeyboardButton("😎 Důvody, proč si zajít na kávu", callback_data='cz_reasons')],
        ]
        q.edit_message_text("Na co se mě můžeš zeptat:", reply_markup=InlineKeyboardMarkup(kb))

def handle_section(update: Update, context: CallbackContext):
    q = update.callback_query
    q.answer()
    q.edit_message_reply_markup(None)
    if q.data in texts:
        q.message.reply_text(texts[q.data])

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(language_selected, pattern='^lang_'))
    dp.add_handler(CallbackQueryHandler(handle_section, pattern='^cz_'))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
