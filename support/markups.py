from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Support', url='t.me/JagoanRedesign'),
            InlineKeyboardButton('Source', url='github.com/JagoanRedesign')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/JagoanRedesign'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
