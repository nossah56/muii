import asyncio

import random

from AbdoX import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





txt = [


" عاوز اي بوشك دا 🙂😒 ",
" قلبو ودقاته وكل حياته❤️🥺  ", 
" مين 🤔  ", 
" نعمين  ", 
"شششش بحبك❤️",
"اندهلي باسمي لــــو ســــمحــت",
"اسمي مستر هانتر يبني",


        ]


        


@app.on_message(filters.command(["يا بوت","بوت"], ""))

async def ahrof(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
