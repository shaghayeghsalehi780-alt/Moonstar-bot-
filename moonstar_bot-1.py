import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import os
TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = 8320580546
ADMIN_USERNAME = "@MoonstarSalehi"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🗣️ Kurse & Preise", callback_data="kurse")],
        [InlineKeyboardButton("📖 Über uns", callback_data="ueber")],
        [InlineKeyboardButton("⭐ Bewertungen", callback_data="bewertungen")],
        [InlineKeyboardButton("📩 Anmeldung", callback_data="anmeldung")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌟 *Willkommen bei Moonstar Salehi!*\n\n"
        "Ich bin dein persönlicher Deutschkurs-Assistent.\n"
        "Was möchtest du wissen?\n\n"
        "👇 Wähle eine Option:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def kurse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🗣️ Sprechkurs — 14 Einheiten", callback_data="kurs_sprechen")],
        [InlineKeyboardButton("🗣️ Sprechkurs + Telc — 26 Einheiten", callback_data="kurs_telc")],
        [InlineKeyboardButton("📚 Wortschatz B2/C1 — 26 Einheiten", callback_data="kurs_wortschatz")],
        [InlineKeyboardButton("🎯 Prüfungsworkshop", callback_data="kurs_workshop")],
        [InlineKeyboardButton("🗓️ Monatlicher Lernplan", callback_data="kurs_plan")],
        [InlineKeyboardButton("🔙 Zurück", callback_data="start")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📚 *Unsere Kurse*\n\nWähle einen Kurs für mehr Details:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def kurs_sprechen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📩 Jetzt anmelden", callback_data="anmeldung")],
        [InlineKeyboardButton("🔙 Zurück", callback_data="kurse")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🗣️ *Sprechkurs — 14 Einheiten*\n\n"
        "⏰ 90 Minuten pro Einheit\n"
        "📅 3 Einheiten pro Woche\n\n"
        "📌 *Inhalt:*\n"
        "• Vorstellen, Präsentation\n"
        "• Diskussion & Planung\n"
        "• Natürliches Sprechen\n"
        "• Aussprache & Selbstvertrauen\n\n"
        "💰 *Preise:*\n"
        "👤 Einzelunterricht: *49$*\n"
        "👥 Gruppenunterricht: *35$*\n\n"
        "🌟 *Moonstar Salehi | @MoonstarSalehi*",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def kurs_telc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📩 Jetzt anmelden", callback_data="anmeldung")],
        [InlineKeyboardButton("🔙 Zurück", callback_data="kurse")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🗣️ *Sprechkurs + Telc B2 — 26 Einheiten*\n\n"
        "⏰ 90 Minuten pro Einheit\n"
        "📅 3 Einheiten pro Woche\n\n"
        "📌 *Inhalt:*\n"
        "• Einheit 1: Theorie & Prüfungsstruktur\n"
        "• Ab Einheit 2: Alle 72 Diskussionsthemen\n"
        "• Planung & Präsentation\n"
        "• Telc B2 Prüfungsvorbereitung\n\n"
        "💰 *Preis:*\n"
        "👤 Einzelunterricht: *91$*\n\n"
        "🌟 *Moonstar Salehi | @MoonstarSalehi*",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def kurs_wortschatz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📩 Jetzt anmelden", callback_data="anmeldung")],
        [InlineKeyboardButton("🔙 Zurück", callback_data="kurse")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📚 *Wortschatz B2/C1 — 26 Einheiten*\n\n"
        "⏰ 90 Minuten pro Einheit\n\n"
        "📖 *Jede Einheit hat 3 Teile:*\n\n"
        "1️⃣ *15 Min — Wörter aus dem Buch Unsicher B2/C1*\n"
        "• 50–100 Wörter pro Thema\n"
        "• Synonyme & Bedeutungen\n"
        "• Beispiele aus dem Alltag\n\n"
        "2️⃣ *15 Min — Podcast zum gleichen Thema*\n"
        "• Aktives Zuhören\n"
        "• So spricht man im echten Leben\n\n"
        "3️⃣ *60 Min — Freies Gespräch mit den gelernten Wörtern*\n"
        "• Wörter direkt anwenden\n"
        "• Natürlich und sicher sprechen\n\n"
        "💡 *Warum diese Methode?*\n"
        "Du begegnest jedem Wort 3x in einer Einheit:\n"
        "lesen → hören → sprechen\n"
        "So bleibt es für immer im Gedächtnis! 🧠\n\n"
        "💰 *Preis:*\n"
        "👤 Einzelunterricht: *104$*\n\n"
        "🌟 *Moonstar Salehi | @MoonstarSalehi*",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def kurs_workshop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📩 Jetzt anmelden", callback_data="anmeldung")],
        [InlineKeyboardButton("🔙 Zurück", callback_data="kurse")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🎯 *Prüfungsworkshop Telc — 1 Einheit*\n\n"
        "⏰ 90 Minuten\n\n"
        "📌 *Inhalt:*\n"
        "• Alle Prüfungsteile werden erklärt\n"
        "• Antworttechniken\n"
        "• Beispielaufgaben\n"
        "• Häufige Fehler & Tipps\n\n"
        "💰 *Preis:*\n"
        "🎯 *7$*\n\n"
        "🌟 *Moonstar Salehi | @MoonstarSalehi*",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def kurs_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📩 Jetzt anmelden", callback_data="anmeldung")],
        [InlineKeyboardButton("🔙 Zurück", callback_data="kurse")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🗓️ *Monatlicher Lernplan*\n\n"
        "📌 *Was bekommst du?*\n"
        "• Persönlicher Plan für 1 Monat\n"
        "• Prüfungsvorbereitung & Sprachtraining\n"
        "• Klare Ziele & Strategie\n"
        "• Für Anfänger und Fortgeschrittene\n\n"
        "💰 *Preis:*\n"
        "🗓️ *5$ pro Monat*\n\n"
        "🌟 *Moonstar Salehi | @MoonstarSalehi*",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def ueber(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🔙 Zurück", callback_data="start")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🌟 *Über Moonstar Salehi*\n\n"
        "Ich bin Shaghayegh Salehi — Deutschlehrerin mit Spezialisierung auf Sprechen.\n\n"
        "🏆 *Telc B2 Sprechen: 75/75 Punkte*\n\n"
        "✅ 3 Jahre Unterrichtserfahrung\n"
        "✅ Schüler aus Iran, Türkei und der ganzen Welt\n"
        "✅ Online-Unterricht via Google Meet\n\n"
        "🎙️ Podcast: @deutscherpod\n"
        "📩 Kontakt: @MoonstarSalehi",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def bewertungen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("✍️ Bewertung schreiben", callback_data="bewertung_schreiben")],
        [InlineKeyboardButton("🔙 Zurück", callback_data="start")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "⭐ *Bewertungen unserer Schüler*\n\n"
        "⭐⭐⭐⭐⭐ Labarania\n"
        "_\"Telc B2: 270/300 — Sehr gut! Danke Moonstar!\"_\n\n"
        "⭐⭐⭐⭐⭐ Konkanas\n"
        "_\"Telc B2: 281/300 — Die beste Lehrerin!\"_\n\n"
        "⭐⭐⭐⭐⭐ Ameneh\n"
        "_\"Sprechen macht jetzt viel mehr Spaß!\"_\n\n"
        "📺 Alle Bewertungen auf unserem Kanal:\n"
        "👉 [DankeMomente](https://t.me/DankeMomente)\n\n"
        "📩 Hast du auch einen Kurs gemacht? Schreib deine Bewertung!",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def bewertung_schreiben(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🔙 Zurück", callback_data="bewertungen")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.user_data["waiting_for_review"] = True
    await query.edit_message_text(
        "✍️ *Schreib deine Bewertung*\n\n"
        "Schreib einfach deine Meinung!\n\n"
        "Beispiel: ⭐⭐⭐⭐⭐ Der Kurs hat mir sehr geholfen!",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def anmeldung(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🔙 Zurück", callback_data="start")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📩 *Anmeldung*\n\n"
        "Schreib direkt an:\n"
        "👉 @MoonstarSalehi\n\n"
        "Oder schick mir hier eine Nachricht!\n\n"
        "🌟 Wir freuen uns auf dich!",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def back_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🗣️ Kurse & Preise", callback_data="kurse")],
        [InlineKeyboardButton("📖 Über uns", callback_data="ueber")],
        [InlineKeyboardButton("⭐ Bewertungen", callback_data="bewertungen")],
        [InlineKeyboardButton("📩 Anmeldung", callback_data="anmeldung")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🌟 *Willkommen bei Moonstar Salehi!*\n\n"
        "Ich bin dein persönlicher Deutschkurs-Assistent.\n"
        "Was möchtest du wissen?\n\n"
        "👇 Wähle eine Option:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    if context.user_data.get("waiting_for_review"):
        context.user_data["waiting_for_review"] = False
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"⭐ Neue Bewertung von {user.first_name} (@{user.username}):\n\n{text}"
        )
        await update.message.reply_text(
            "✅ Danke für deine Bewertung! 🌟"
        )
    else:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 Neue Nachricht von {user.first_name} (@{user.username}):\n\n{text}"
        )
        await update.message.reply_text(
            "✅ Deine Nachricht wurde weitergeleitet!\n"
            "📩 @MoonstarSalehi meldet sich bald. 🌟"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(kurse, pattern="^kurse$"))
    app.add_handler(CallbackQueryHandler(kurs_sprechen, pattern="^kurs_sprechen$"))
    app.add_handler(CallbackQueryHandler(kurs_telc, pattern="^kurs_telc$"))
    app.add_handler(CallbackQueryHandler(kurs_wortschatz, pattern="^kurs_wortschatz$"))
    app.add_handler(CallbackQueryHandler(kurs_workshop, pattern="^kurs_workshop$"))
    app.add_handler(CallbackQueryHandler(kurs_plan, pattern="^kurs_plan$"))
    app.add_handler(CallbackQueryHandler(ueber, pattern="^ueber$"))
    app.add_handler(CallbackQueryHandler(bewertungen, pattern="^bewertungen$"))
    app.add_handler(CallbackQueryHandler(bewertung_schreiben, pattern="^bewertung_schreiben$"))
    app.add_handler(CallbackQueryHandler(anmeldung, pattern="^anmeldung$"))
    app.add_handler(CallbackQueryHandler(back_start, pattern="^start$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🌟 Moonstar Bot läuft...")
    app.run_polling()

from threading import Thread
import http.server

def run_server():
    server = http.server.HTTPServer(('0.0.0.0', 8080), http.server.BaseHTTPRequestHandler)
    server.serve_forever()
    
Thread(target=run_server, daemon=True).start()

if __name__ == "__main__":
   main()

