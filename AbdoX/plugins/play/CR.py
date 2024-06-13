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
    command("الاوامر")
)
async def هانتر_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/efa394c06f92186cd5277.jpg",
        caption=f"""**⩹━𓍹𓋹𓍻⊷━⌞𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝━⊶𓍹𓋹𓍻━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس هانتر \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝━⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝⚡", url=f"https://t.me/huntersource"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def هانتر_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**
𓍹𓋹𓍻¦ اهلا بك عزيزي في قسم اوامر التشغيل في الجروبات
𓍹𓋹𓍻¦ تشغيل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ فديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ #فيديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ #فديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ {NAME_BOT} + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /فيديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /ق شغل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /تشغيل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ cvplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ cplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /vplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /play + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ #تشغيل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ فيديو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ سورة + اسم السورة 
𓍹𓋹𓍻¦ cvplayforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ cplayforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ vplayforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ playforce + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ /cvplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ vplay + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ play + اسم الاغنيه/السوره

**⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def هانتر_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⌯𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**
𓍹𓋹𓍻¦ اهلا بك عزيزي في قسم اوامر التشغيل في القنوات
𓍹𓋹𓍻¦ شغل + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ قناه + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ مانو + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ ق + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ اغاني + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ . + اسم الاغنيه/السوره
𓍹𓋹𓍻¦ / + اسم الاغنيه/السوره
**⩹⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def هانتر_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⌯⊶𓍹𓋹𓍻━⩺**
𓍹𓋹𓍻¦ اهلا بك عزيزي في قسم اوامر تشغيل الادمن
𓍹𓋹𓍻¦ رفع ثانوي
𓍹𓋹𓍻¦ تنزيل ثانوي
𓍹𓋹𓍻¦ قائمة الثانويين
𓍹𓋹𓍻¦ رفع ادمن
𓍹𓋹𓍻¦ تنزيل ادمن
𓍹𓋹𓍻¦ قائمة الادمن
𓍹𓋹𓍻¦ حظر
𓍹𓋹𓍻¦ الغاء الحظر
𓍹𓋹𓍻¦ المحظورين
𓍹𓋹𓍻¦ حظر عام
𓍹𓋹𓍻¦ الغاء الحظر العام
𓍹𓋹𓍻¦ المحظورين عام
𓍹𓋹𓍻¦ اونلاين
𓍹𓋹𓍻¦ اذاعه
𓍹𓋹𓍻¦ تحديث
𓍹𓋹𓍻¦ logger
𓍹𓋹𓍻¦ ريلود
𓍹𓋹𓍻¦ وقف
𓍹𓋹𓍻¦ كمل
𓍹𓋹𓍻¦ اسكت
𓍹𓋹𓍻¦ اتكلم
𓍹𓋹𓍻¦ ايقاف
𓍹𓋹𓍻¦ تخطي
𓍹𓋹𓍻¦ @all
𓍹𓋹𓍻¦ all stop
𓍹𓋹𓍻¦ يوتيوب / تنزيل
𓍹𓋹𓍻¦ playing
𓍹𓋹𓍻¦ القائمه
𓍹𓋹𓍻¦ حذف القائمه
𓍹𓋹𓍻¦ تحديث
𓍹𓋹𓍻¦ الاحصائيات
𓍹𓋹𓍻¦ لايف
𓍹𓋹𓍻¦ مساعده
𓍹𓋹𓍻¦ الاعدادت
𓍹𓋹𓍻¦ بينج

**⩹━𓍹𓋹𓍻⊷⌯⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝⌯⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def هانتر_back(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/efa394c06f92186cd5277.jpg",
        caption=f"""**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝━⊶𓍹𓋹𓍻━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس هانتر \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━𓍹𓋹𓍻⊷━⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺ ⌝━⊶𓍹𓋹𓍻━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞𓏺َِ𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺⌝⚡", url=f"https://t.me/huntersource"),
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
    
    @app.on_message(command(["معلوماته", "كشف"]) & filters.group & ~filters.edited) 
async def hshs(client: Client, message: Message):      
    usr = await client.get_users(message.reply_to_message.from_user.id)
    name = usr.first_name#
    user_id = message.reply_to_message.from_user.id#
    chat_idd = message.chat.id#
    chat_username = f"@{message.chat.username}" #
    chat_name = message.chat.title#
    username = f"@{message.reply_to_message.from_user.username}"#
    async for photo in client.iter_profile_photos(message.reply_to_message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**[𓍹𓋹𓍻⌞𓏺• ⌞ ⩹━⊷⌯ 𓏺𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐 •˼⁩](https://t.me/huntersource)\n\n🐉 ¦ ɴᴀᴍᴇ : {name}\n🤡 ¦ ᴜѕᴇ : {username}\n🔥 ¦ ɪᴅ : `{user_id}`\n🔅 ¦ ɪᴅ ᴄʜᴀᴛ : `{chat_idd}`\n💭 ¦ ᴄʜᴀᴛ : {chat_name}\n🐊 ¦ ɢʀᴏᴜᴘ : {chat_username} \n**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.reply_to_message.from_user.username}")
                ],
            ]
        ),
    )     



@app.on_message(
    command(["بايو","البايو"])
    & filters.group
    & ~filters.edited
)
async def biio(client, message):
  nq = await client.get_chat(message.from_user.id)
  bio = nq.bio
  await message.reply_text(bio
  )
@app.on_message(
    command(["شخصيتي", "معلوماتي", "شخصيه"])
    & filters.group
    & ~filters.edited
)
async def ppdi(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**• انـت »   {message.from_user.mention()} يا قلبي ياناس🔥😮‍💨**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
 
 
 
 
@app.on_message(command(["تحويل_لصوره", "تحويل الصوره"]))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



@app.on_message(command(["الجروب", "جروب"]) & filters.group & ~filters.edited)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**🐲 ¦ الاسم » {chat_name}\n🚸 ¦ ايدي الجروب »  -{chat_idd}\n🐊 ¦ رابط » {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    
    @app.on_message(command(["صاحب الخرابه", "المنشي"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
            f = "administrators"
            async for member in client.iter_chat_members(chat_id, filter=f):
               if member.status == "creator":
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🎃 ¦𝙸𝙳 :`{m.id}`\n💌 ¦𝙱𝙸𝙾 :{m.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{message.chat.id}`",reply_markup=key)
                 else:
                    return await message.reply("• " + member.user.mention)
                    
                    
   

   
@app.on_message(command(["اسمي", "شن اسمي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""") 

        

array = []
@app.on_message(command(["@all", "تاك","تاك للكل"]) & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("**التاك قيد التشغيل حالياً ،**")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["administrator", "creator"]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🖱️**")
    return
  await message.reply_text("**جاري بدأ المنشن ، لايقاف الامر اضغط **\n اكتب خلاص او اكتب وقف منشن")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("كلمهم","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.iter_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ،"
       if i == 5:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@app.on_message(command(["وقف منشن", "/cancel","خلاص"]))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["administrator", "creator"]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🖱️")
    return
  if message.chat.id not in array:
     await message.reply("**المنشن متوقف بالفعل**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("**تم ايقاف المنشن بنجاح✅**")
    return
    