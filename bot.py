from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8951416380:AAEryBMAeEQ5vRyKHrkao89otfOioNMt47A"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 سرورها", callback_data="plans")],
        [InlineKeyboardButton("🔥 خرید بالای 50 گیگ (تخفیف ویژه)", callback_data="vip")],
        [InlineKeyboardButton("💬 پشتیبانی", url="https://t.me/pmnetx")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 به ربات فروش اینترنت خوش آمدی!\n\n"
        "از گزینه‌های زیر انتخاب کن:",
        reply_markup=reply_markup
    )

# کلیک دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "plans":
        keyboard = [
            [InlineKeyboardButton("10GB - 175", callback_data="buy_10")],
            [InlineKeyboardButton("20GB - 325", callback_data="buy_20")],
            [InlineKeyboardButton("50GB - 775", callback_data="buy_50")],
        ]
        await query.edit_message_text(
            "📦 لیست سرورها:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "vip":
        await query.edit_message_text(
            "🔥 خرید بالای 50 گیگ شامل تخفیف ویژه است!\n\n"
            "برای سفارش وارد پشتیبانی شوید: @pmnetx"
        )

    elif query.data.startswith("buy_"):
        await query.edit_message_text(
            "✅ سفارش ثبت شد!\nبرای تکمیل خرید به پشتیبانی پیام بده: @pmnetx"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
