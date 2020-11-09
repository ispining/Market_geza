import telebot
from telebot import types
import config
import text
import logging
import he
import ru
import en
import sqlite3

db = sqlite3.connect("server.db")
sql = db.cursor()




cmy = config.my

logger = telebot.logger
telebot.logger.setLevel(logging.ERROR) # Outputs debug messages to console.


bot = telebot.TeleBot(config.token, parse_mode=None)





@bot.message_handler(commands=['start'])
def welcome(message):
        if message.chat.type == "private":
            keyboard = types.InlineKeyboardMarkup()
            group_button = types.InlineKeyboardButton(config.my.group_button, url=config.my.group_button_url)
            keyboard.row(group_button)
            weed_info_button = types.InlineKeyboardButton(config.my.weed_info_button,
                                                          callback_data=config.my.weed_info_button_call)
            keyboard.row(weed_info_button)
            reviews_button = types.InlineKeyboardButton(config.my.reviews_button,
                                                        callback_data=config.my.reviews_button_call)
            keyboard.row(reviews_button)
            en_button = types.InlineKeyboardButton(config.en, callback_data=config.en_call)
            he_button = types.InlineKeyboardButton(config.he, callback_data=config.he_call)
            ru_button = types.InlineKeyboardButton(config.ru, callback_data=config.ru_call)
            keyboard.row(he_button, ru_button, en_button)
            f = open('market.jpg', 'rb')
            bot.send_photo(message.chat.id, f, config.my.welcome_message, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda message:True)
def calls(call):
    if call.data == "en":
        config.my = en
        keyboard = types.InlineKeyboardMarkup()
        group_button = types.InlineKeyboardButton(config.my.group_button, url=config.my.group_button_url)
        keyboard.row(group_button)
        weed_info_button = types.InlineKeyboardButton(config.my.weed_info_button, callback_data=config.my.weed_info_button_call)
        keyboard.row(weed_info_button)
        reviews_button = types.InlineKeyboardButton(config.my.reviews_button, callback_data=config.my.reviews_button_call)
        keyboard.row(reviews_button)
        en_button = types.InlineKeyboardButton(config.en, callback_data=config.en_call)
        he_button = types.InlineKeyboardButton(config.he, callback_data=config.he_call)
        ru_button = types.InlineKeyboardButton(config.ru, callback_data=config.ru_call)
        keyboard.row(he_button,ru_button,en_button)
        f = open('market.jpg', 'rb')
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, f, config.my.welcome_message, reply_markup=keyboard)

    elif call.data == "ru":
        config.my = ru
        keyboard = types.InlineKeyboardMarkup()
        group_button = types.InlineKeyboardButton(config.my.group_button, url=config.my.group_button_url)
        keyboard.row(group_button)
        weed_info_button = types.InlineKeyboardButton(config.my.weed_info_button,
                                                      callback_data=config.my.weed_info_button_call)
        keyboard.row(weed_info_button)
        reviews_button = types.InlineKeyboardButton(config.my.reviews_button,
                                                    callback_data=config.my.reviews_button_call)
        keyboard.row(reviews_button)
        en_button = types.InlineKeyboardButton(config.en, callback_data=config.en_call)
        he_button = types.InlineKeyboardButton(config.he, callback_data=config.he_call)
        ru_button = types.InlineKeyboardButton(config.ru, callback_data=config.ru_call)
        keyboard.row(he_button, ru_button, en_button)
        f = open('market.jpg', 'rb')
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, f, config.my.welcome_message, reply_markup=keyboard)

    elif call.data == "he":
        config.my = he
        keyboard = types.InlineKeyboardMarkup()
        group_button = types.InlineKeyboardButton(config.my.group_button, url=config.my.group_button_url)
        keyboard.row(group_button)
        weed_info_button = types.InlineKeyboardButton(config.my.weed_info_button,
                                                      callback_data=config.my.weed_info_button_call)
        keyboard.row(weed_info_button)
        reviews_button = types.InlineKeyboardButton(config.my.reviews_button,
                                                    callback_data=config.my.reviews_button_call)
        keyboard.row(reviews_button)
        en_button = types.InlineKeyboardButton(config.en, callback_data=config.en_call)
        he_button = types.InlineKeyboardButton(config.he, callback_data=config.he_call)
        ru_button = types.InlineKeyboardButton(config.ru, callback_data=config.ru_call)
        keyboard.row(he_button, ru_button, en_button)
        f = open('market.jpg', 'rb')
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, f, config.my.welcome_message, reply_markup=keyboard)

    elif call.data == "home":
        keyboard = types.InlineKeyboardMarkup()
        group_button = types.InlineKeyboardButton(config.my.group_button, url=config.my.group_button_url)
        keyboard.row(group_button)
        weed_info_button = types.InlineKeyboardButton(config.my.weed_info_button,
                                                      callback_data=config.my.weed_info_button_call)
        keyboard.row(weed_info_button)
        reviews_button = types.InlineKeyboardButton(config.my.reviews_button,
                                                    callback_data=config.my.reviews_button_call)
        keyboard.row(reviews_button)
        en_button = types.InlineKeyboardButton(config.en, callback_data=config.en_call)
        he_button = types.InlineKeyboardButton(config.he, callback_data=config.he_call)
        ru_button = types.InlineKeyboardButton(config.ru, callback_data=config.ru_call)
        keyboard.row(he_button, ru_button, en_button)
        f = open('market.jpg', 'rb')
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, f, config.my.welcome_message, reply_markup=keyboard)

    elif call.data == 'weed_info':
        keyboard = types.InlineKeyboardMarkup()
        weed1 = types.InlineKeyboardButton(config.my.jeck, callback_data="weed1")
        keyboard.row(weed1)
        weed2 = types.InlineKeyboardButton(config.my.chernobil, callback_data="weed2")
        keyboard.row(weed2)
        weed3 = types.InlineKeyboardButton(config.my.flash, callback_data="weed3")
        keyboard.row(weed3)
        weed4 = types.InlineKeyboardButton(config.my.pharma, callback_data="weed4")
        keyboard.row(weed4)
        weed5 = types.InlineKeyboardButton(config.my.nortern, callback_data="weed5")
        keyboard.row(weed5)
        weed6 = types.InlineKeyboardButton(config.my.harle, callback_data="weed6")
        keyboard.row(weed6)
        weed7 = types.InlineKeyboardButton(config.my.sour_zunami, callback_data="weed7")
        keyboard.row(weed7)
        weed8 = types.InlineKeyboardButton(config.my.peni, callback_data="weed8")
        keyboard.row(weed8)
        back = types.InlineKeyboardButton(config.my.back, callback_data="home")
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id,open('market.jpg', 'rb'),
                       caption=config.my.weed_info_text, reply_markup=keyboard)

    elif call.data == "weed1":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("jeck.jpg","rb") , caption=config.my.jeck_text, reply_markup=keyboard)

    elif call.data == "weed2":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("Chernobyl.jpg","rb") , caption=config.my.chernobyl_text, reply_markup=keyboard)

    elif call.data == "weed3":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("plush.jpg","rb") , caption=config.my.flash_text, reply_markup=keyboard)
    elif call.data == "weed4":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("pandora.jpg","rb") , caption=config.my.pharma_text, reply_markup=keyboard)
    elif call.data == "weed5":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("nortern.jpg","rb") , caption=config.my.nortern_text, reply_markup=keyboard)
    elif call.data == "weed6":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("hk.jpg","rb") , caption=config.my.harle_text, reply_markup=keyboard)
    elif call.data == "weed7":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("znm.jpg","rb") , caption=config.my.sour_zunami_text, reply_markup=keyboard)
    elif call.data == "weed8":
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_photo(call.message.chat.id, open("pw.jpg","rb") , caption=config.my.peni_text, reply_markup=keyboard)



    elif call.data == config.my.reviews_button_call:
        keyboard = types.InlineKeyboardMarkup()
        write_button = types.InlineKeyboardButton(config.my.write_button, callback_data=config.my.write_button_call)
        read_button = types.InlineKeyboardButton(config.my.read_button, url=config.my.read_button_url)
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(write_button)
        keyboard.row(read_button)
        keyboard.row(back)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=config.my.reviews_text,
                                 reply_markup=keyboard)

    elif call.data == config.my.write_button_call:
        keyboard = types.InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(config.one_star, callback_data="a1")
        a2 = types.InlineKeyboardButton(config.two_stars, callback_data="a2")
        a3 = types.InlineKeyboardButton(config.three_stars, callback_data="a3")
        a4 = types.InlineKeyboardButton(config.four_stars, callback_data="a4")
        a5 = types.InlineKeyboardButton(config.five_stars, callback_data="a5")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(a5)
        keyboard.row(a4)
        keyboard.row(a3)
        keyboard.row(a2)
        keyboard.row(a1)
        keyboard.row(back)
        bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, config.my.delivery, reply_markup=keyboard)
    elif call.data == "a1":
        config.result1 = config.one_star
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(config.one_star, callback_data="b1")
        b2 = types.InlineKeyboardButton(config.two_stars, callback_data="b2")
        b3 = types.InlineKeyboardButton(config.three_stars, callback_data="b3")
        b4 = types.InlineKeyboardButton(config.four_stars, callback_data="b4")
        b5 = types.InlineKeyboardButton(config.five_stars, callback_data="b5")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(b5)
        keyboard.row(b4)
        keyboard.row(b3)
        keyboard.row(b2)
        keyboard.row(b1)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text=config.my.quality, reply_markup=keyboard)

    elif call.data == "a2":
        config.result1 = config.two_stars
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(config.one_star, callback_data="b1")
        b2 = types.InlineKeyboardButton(config.two_stars, callback_data="b2")
        b3 = types.InlineKeyboardButton(config.three_stars, callback_data="b3")
        b4 = types.InlineKeyboardButton(config.four_stars, callback_data="b4")
        b5 = types.InlineKeyboardButton(config.five_stars, callback_data="b5")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(b5)
        keyboard.row(b4)
        keyboard.row(b3)
        keyboard.row(b2)
        keyboard.row(b1)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.quality, reply_markup=keyboard)
    elif call.data == "a3":
        config.result1 = config.three_stars
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(config.one_star, callback_data="b1")
        b2 = types.InlineKeyboardButton(config.two_stars, callback_data="b2")
        b3 = types.InlineKeyboardButton(config.three_stars, callback_data="b3")
        b4 = types.InlineKeyboardButton(config.four_stars, callback_data="b4")
        b5 = types.InlineKeyboardButton(config.five_stars, callback_data="b5")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(b5)
        keyboard.row(b4)
        keyboard.row(b3)
        keyboard.row(b2)
        keyboard.row(b1)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.quality, reply_markup=keyboard)

    elif call.data == "a4":
        config.result1 = config.four_stars
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(config.one_star, callback_data="b1")
        b2 = types.InlineKeyboardButton(config.two_stars, callback_data="b2")
        b3 = types.InlineKeyboardButton(config.three_stars, callback_data="b3")
        b4 = types.InlineKeyboardButton(config.four_stars, callback_data="b4")
        b5 = types.InlineKeyboardButton(config.five_stars, callback_data="b5")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(b5)
        keyboard.row(b4)
        keyboard.row(b3)
        keyboard.row(b2)
        keyboard.row(b1)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.quality, reply_markup=keyboard)

    elif call.data == "a5":
        config.result1 = config.five_stars
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(config.one_star, callback_data="b1")
        b2 = types.InlineKeyboardButton(config.two_stars, callback_data="b2")
        b3 = types.InlineKeyboardButton(config.three_stars, callback_data="b3")
        b4 = types.InlineKeyboardButton(config.four_stars, callback_data="b4")
        b5 = types.InlineKeyboardButton(config.five_stars, callback_data="b5")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(b5)
        keyboard.row(b4)
        keyboard.row(b3)
        keyboard.row(b2)
        keyboard.row(b1)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.quality, reply_markup=keyboard)
    elif call.data == "b1":
        config.result2 = config.one_star
        keyboard = types.InlineKeyboardMarkup()
        c1 = types.InlineKeyboardButton(config.my.cost_100, callback_data="c1")
        c2 = types.InlineKeyboardButton(config.my.cost_90, callback_data="c2")
        c3 = types.InlineKeyboardButton(config.my.cost_80, callback_data="c3")
        c4 = types.InlineKeyboardButton(config.my.cost_70, callback_data="c4")
        c5 = types.InlineKeyboardButton(config.my.cost_60, callback_data="c5")
        c6 = types.InlineKeyboardButton(config.my.cost_50, callback_data="c6")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(c1,c2,c3,c4,c5)
        keyboard.row(c6)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.cost, reply_markup=keyboard)

    elif call.data == "b2":
        config.result2 = config.two_stars
        keyboard = types.InlineKeyboardMarkup()
        c1 = types.InlineKeyboardButton(config.my.cost_100, callback_data="c1")
        c2 = types.InlineKeyboardButton(config.my.cost_90, callback_data="c2")
        c3 = types.InlineKeyboardButton(config.my.cost_80, callback_data="c3")
        c4 = types.InlineKeyboardButton(config.my.cost_70, callback_data="c4")
        c5 = types.InlineKeyboardButton(config.my.cost_60, callback_data="c5")
        c6 = types.InlineKeyboardButton(config.my.cost_50, callback_data="c6")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(c1, c2, c3, c4, c5)
        keyboard.row(c6)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.cost, reply_markup=keyboard)

    elif call.data == "b3":
        config.result2 = config.three_stars
        keyboard = types.InlineKeyboardMarkup()
        c1 = types.InlineKeyboardButton(config.my.cost_100, callback_data="c1")
        c2 = types.InlineKeyboardButton(config.my.cost_90, callback_data="c2")
        c3 = types.InlineKeyboardButton(config.my.cost_80, callback_data="c3")
        c4 = types.InlineKeyboardButton(config.my.cost_70, callback_data="c4")
        c5 = types.InlineKeyboardButton(config.my.cost_60, callback_data="c5")
        c6 = types.InlineKeyboardButton(config.my.cost_50, callback_data="c6")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(c1,c2,c3,c4,c5)
        keyboard.row(c6)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.cost, reply_markup=keyboard)

    elif call.data == "b4":
        config.result2 = config.four_stars
        keyboard = types.InlineKeyboardMarkup()
        c1 = types.InlineKeyboardButton(config.my.cost_100, callback_data="c1")
        c2 = types.InlineKeyboardButton(config.my.cost_90, callback_data="c2")
        c3 = types.InlineKeyboardButton(config.my.cost_80, callback_data="c3")
        c4 = types.InlineKeyboardButton(config.my.cost_70, callback_data="c4")
        c5 = types.InlineKeyboardButton(config.my.cost_60, callback_data="c5")
        c6 = types.InlineKeyboardButton(config.my.cost_50, callback_data="c6")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(c1,c2,c3,c4,c5)
        keyboard.row(c6)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.cost, reply_markup=keyboard)

    elif call.data == "b5":
        config.result2 = config.five_stars
        keyboard = types.InlineKeyboardMarkup()
        c1 = types.InlineKeyboardButton(config.my.cost_100, callback_data="c1")
        c2 = types.InlineKeyboardButton(config.my.cost_90, callback_data="c2")
        c3 = types.InlineKeyboardButton(config.my.cost_80, callback_data="c3")
        c4 = types.InlineKeyboardButton(config.my.cost_70, callback_data="c4")
        c5 = types.InlineKeyboardButton(config.my.cost_60, callback_data="c5")
        c6 = types.InlineKeyboardButton(config.my.cost_50, callback_data="c6")
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(c1,c2,c3,c4,c5)
        keyboard.row(c6)
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.cost, reply_markup=keyboard)



    elif call.data == "c1":
        config.result3 = config.my.cost_100
        config.result_text = "empty"
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.about_result)

    elif call.data == "c2":
        config.result3 = config.my.cost_90
        config.result_text = "empty"
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.about_result)

    elif call.data == "c3":
        config.result3 = config.my.cost_80
        config.result_text = "empty"
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.about_result)

    elif call.data == "c4":
        config.result3 = config.my.cost_70
        config.result_text = "empty"
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.about_result)

    elif call.data == "c5":
        config.result3 = config.my.cost_60
        config.result_text = "empty"
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.about_result)
    elif call.data == "c6":
        config.result3 = config.my.cost_50
        config.result_text = "empty"
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(config.my.back, callback_data='home')
        keyboard.row(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=config.my.about_result)




    elif call.data == config.my.confirm_call:
        bot.send_message(chat_id=config.tunnel_id,disable_notification=True,
                         text=config.r_text)



@bot.message_handler(content_types=['text'])
def about_dealer(message):
    if config.result_text == "empty":
        config.result_text = message.text
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton("לעבור לבוט של מרקט", url="https://t.me/market_gezabot/")
        keyboard.row(back)
        config.r_text = "הלקוח:   "+ message.chat.username +he.delivery_result + config.result1 + "\n" + he.quality_result + config.result2 + \
                        "\n"+ he.cost_result + config.result3 + he.about_result + config.result_text
        bot.send_message(config.tunnel_id, config.r_text, disable_notification=True, reply_markup=keyboard)
        bot.send_message(message.chat.id, config.my.ok)





bot.polling(none_stop=True, timeout=10000)

