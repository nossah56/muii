#_____كسمك تحياتي 
#_____@EU_TM

import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from AbdoX import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/huntersource/71",
        caption=f"𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/yyyyybbh"), 
                 InlineKeyboardButton(
                   " 𝐒𝐎𝐔𝐑𝐂𝐄",       url=f"https://t.me/huntersource"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "𝑫𝑬𝑽 𝑯𝑼𝑵𝑻𝑬𝑹 ", url=f"https://t.me/U_7h1"), 
                   
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )















@app.on_message(
    command(["مميزات","مميزات هانتر"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس هانتر ميوزك\n
⩹━𓍹𓋹𓍻⊷⌯⌞ ⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺

𓍹𓋹𓍻قايمه مميزات سورس هانتر 

𓍹𓋹𓍻ميزه ⦂ المطور بيجيب المطور البوت 
𓍹𓋹𓍻ميزه ⦂ تبيه بفتح+قفل المكالمه
𓍹𓋹𓍻ميزه ⦂ ترحيب دخول و خروج الاعضاء 
𓍹𓋹𓍻ميزه ⦂ جروب بيجيب الجروب+الرابط+ايدي
𓍹𓋹𓍻ميزه ⦂ قول البوت بيقول بالكلمه اللي بتقولها 
𓍹𓋹𓍻ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
𓍹𓋹𓍻ميزه ⦂ تلغراف ميديا بردعالصوره
𓍹𓋹𓍻ميزه ⦂ ايدي بالرد بالصوره
𓍹𓋹𓍻ميزه ⦂ صورتي يرد بالصوره ونسبه
𓍹𓋹𓍻ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
𓍹𓋹𓍻ميزه ⦂ الصوتيه..ف المكالمه
𓍹𓋹𓍻ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد فالمكالمه
𓍹𓋹𓍻ميزه ⦂ بث مباشر للقنوات 
𓍹𓋹𓍻ميزه ⦂ اسمي بيجب الاسم
𓍹𓋹𓍻ميزه ⦂ سورس بيجب السورس
𓍹𓋹𓍻ميزه ⦂ حظر+كتم ميوزك
𓍹𓋹𓍻ميزه ⦂ كشف
𓍹𓋹𓍻ميزه ⦂ منشن لكل الاعضاء
𓍹𓋹𓍻ميزه ⦂ انا من
𓍹𓋹𓍻ميزه ⦂ رتبتي
𓍹𓋹𓍻ميزه ⦂ مبرمج
𓍹𓋹𓍻ميزه ⦂ المنشئ+المالك
𓍹𓋹𓍻ميزه ⦂ الاحصائيات
𓍹𓋹𓍻ميزه ⦂ كيب المطور من خلاله تتحكم في الحساب المساعد
𓍹𓋹𓍻ميزه ⦂ الاذكار
𓍹𓋹𓍻ميزه ⦂ تبيه بوقت صلاه
𓍹𓋹𓍻ميزه ⦂ دعوه في مكالمه
𓍹𓋹𓍻ميزه ⦂  دعوه فالخاص متاع البوت
𓍹𓋹𓍻ميزه ⦂ تنبيه..بانضمام بوت في الجروبات
𓍹𓋹𓍻ميزه ⦂ غنيلي 
𓍹𓋹𓍻ميزه ⦂ خروج المساعد من جروبات لعدم تقطيع صوت..البوت
𓍹𓋹𓍻ميزه ⦂ اسال/اصراحه
𓍹𓋹𓍻ميزه ⦂ نكت
𓍹𓋹𓍻ميزه ⦂ ذكاء اصتناعي 

⌞ ⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺

""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞ ⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⚡", url=f"https://t.me/huntersource"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )



@app.on_message(
    command(["صاصا" , "المبرمج","مطور السورس","مصطفي","ديشا","مصطفى","مبرمج السورس","عمك"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("U_7h1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"مــعلومـات مــطور الـسـورس \n\n dev :{name}\n\n user :@{usr.username}\n\n id :`{usr.id}`\n\n boi :{usr.bio}\n\n 𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )







@app.on_message(
    command(["مطورين هانتر","المطورين","مطورين"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/efa394c06f92186cd5277.jpg",
        caption=f"""**⩹━𒍮⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶𒍮━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين هانتر ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━𒍮⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹 🦋⌯⊶𒍮━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𒍮᚜⎖᳒𝑺𝑨𝑺𝑨 𖤐𒍮", url=f"https://t.me/U_7h1"), 
                 ],[
                    InlineKeyboardButton(
                        "𒍮᚜𝑴𝑨𝑵𝑫𝑶𝑶᚛𒍮", url=f"https://t.me/M_2A_E_S"),
                    InlineKeyboardButton(
                        "𒍮᚜𝑺𝑼𝑷𝑷𝑶𝑹𝑻┋☬᚛𒍮", url=f"https://t.me/yyyyybbh"),
                ],[
                    InlineKeyboardButton(
                        "𒍮᚜𝒀𝑶𝑺𝑹᚛𒍮", url=f"https://t.me/Yosr3456"),
                ],[
                    InlineKeyboardButton(
                        "𒍮𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹  🦋", url=f"https://t.me/huntersource"),
                ],

            ]

        ),

    )


@app.on_message(
    command(["مطور2" , "احمد","ماندو"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("M_2A_E_S")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"مــعلـومـات مــبرمـج الـسـورس  \n\n dev :{name}\n\n user :@{usr.username}\n\n id :`{usr.id}`\n\n bio :{usr.bio}\n\n𝐒𝐎𝐔𝐑𝐂𝐄 𝑯𝑼𝑵𝑻𝑬𝑹", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
                  )

@app.on_message(
    command(["ايدي","id",])
    & filters.group
    & ~filters.edited
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f""" - ꪀᥲ️︎ꪔᥱ︎ :{message.from_user.mention}\n- u᥉ᥱ︎ɾ :@{message.from_user.username}\n- Ꭵძ . :`{message.from_user.id}`\nႦᎥ᥆ :{usr.bio}\nᥴ𝗁ᥲ️ƚ: {message.chat.title}\n𝚒𝚍 𝚐𝚛𝚘𝚞𝚋 :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )