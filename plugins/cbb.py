#(Â©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>â—‹ Creator : <a href='tg://user?id={OWNER_ID}'>@Sksksk99</a>\nâ—‹ Language : <code>Python3</code>\nâ—‹ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\nâ—‹ Source Code : <a href='@SKsksk99'>Click here</a>\nâ—‹ Channel : @INDIAHACKER_ICS\nâ—‹ Hacking and course : @INDIAHACKER_ICS</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ðŸ”’ Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
