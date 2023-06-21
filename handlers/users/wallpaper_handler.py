import uuid

from aiogram import types
from loader import dp


from utils.misc import images_parsing


@dp.message_handler()
async def get_wallpaper_name(message: types.Message):
    images_list = images_parsing.images_list(message.text)
    print(images_list)






@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    print(query.query)
    if query.query == "":
        print('true')
        images_list = images_parsing.images_list("python")
    else:    
        images_list = images_parsing.images_list(query.query)

    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id=data["id"],
                photo_url=data["img_thumb"],
                thumb_url=data["img_thumb"],
                caption=data["title"],
                
            ) for data in images_list[:20]
        ]
    )