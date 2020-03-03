import vk_api
import threading
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import *
from vk_api.utils import get_random_id
import wikipedia
status_of_game = {}
from func import game
from func import magic_ball
from func import rand


def menu():
    if event.from_user:
        try:
            if not event.user_id in status_of_game:
                status_of_game.update({event.user_id : [0,0]})
            elif 'дата' == event.text.lower() or 'число' == event.text.lower() or 'время' in event.text.lower():
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                 message=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
            elif 'вики' in event.text.lower() or 'wiki' in event.text.lower():
                try:
                    text = event.text[5:]
                    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                     message='Вот что я нашёл: \n' + str(wikipedia.summary(text)))
                except:
                    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                     message='Вводи корректный запрос!')
            elif 'игра' == event.text.lower() or event.text.lower() == 'game' or event.text.lower() == 'еще' or event.text.lower() == 'стоп':
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                 message=
                                 game(event.user_id, event.text.lower(), status_of_game))
            elif 'волшебный шар ' in event.text.lower() or 'шар правды ' in event.text.lower():
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                 message=magic_ball())
            elif 'случайное число ' in event.text.lower() or 'рандом ' in event.text.lower():
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                 message=rand(event.text.lower()))

        except:
            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                             message='Введён некорректный запрос, попробуйте ещё раз!')
        finally:
            if status_of_game[event.user_id][0] == 0:
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=
            'Если хотите узнать текущее время, введите Дата,\n'
            'Если хотите найти что то в Википедии, введите Wiki/Вики и запрос через пробел.\n'
            'Если вы хотите сыграть в игру 21 очко, введите Game/Игра.\n'
            'Если вы хотите спросить что-либо у волшебного шара правды, введите Шар правды/Волшебный шар и задайте вопрос в формате: Шар правды Я красавчик?\n'
            'Если вы хотите получить случайное число в нужном вам промежутке- введите запрос в формате рандом 10 20.\n')
            else:
                pass


threads = []
users = []
wikipedia.set_lang("RU")
vk_session = vk_api.VkApi(token='')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        user = event.user_id
        if user not in users:
            users.append(user)
            print(users)
            threads.append(threading.Thread(target=menu()))
            print(threads)
        users = []

