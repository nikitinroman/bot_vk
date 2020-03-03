import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import threading
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import wikipedia
from random import randint



def game(user_id, text, status_of_game):
    message = ''
    lst = {2: 'Валет', 3: 'Дама', 4: 'Король', 6: 'Шестёрка', 7: 'Семёрка', 8: 'Восьмёрка', 9: 'Девятка', 10: 'Десятка',
           11: 'Туз'}
    if status_of_game[user_id][0] == 0:
        status_of_game.update({user_id: []})
        a = randint(2, 11)
        if a == 5:
            a += 1
        a1 = lst[a]
        b = randint(2, 11)
        if b == 5:
            b += 1
        b1 = lst[b]
        score = a + b
        status_of_game.update({user_id : [1, score]})
        message += 'Вам выпали ' + a1 + ' И ' + b1 + ', Ваш счёт: ' + str(score)
        if score > 21:
            message += '\nВам выпало более 21 очка, вы проиграли!'
            status_of_game.update({user_id : [0, 0]})
        else:
            message += '\nЕсли хотите продолжить, введите Еще либо Стоп, если закончить'
        return message

    elif status_of_game[user_id][0] != 0:
        score = status_of_game[user_id][1]
        if text.lower() == 'еще' or text.lower() == 'ещё':
            a = randint(2, 11)
            if a == 5:
                a += 1
            score += a
            status_of_game[user_id][1] = score
            a1 = lst[a]
            if score > 21:
                message = 'Вам выпала карта ' + a1 + ' , Ваш счёт: ' + str(
                                     score) + ' Вы проиграли!'
                # status_of_game[user_id][0] = 0
                # status_of_game[user_id][1] = 0
                status_of_game.update({user_id: [0, 0]})
                return message
            else:
                message = 'Вам выпала карта ' + a1 + ' , Ваш счёт: ' + str(score)
                message += '\nЕсли хотите продолжить, введите Еще, если нет- Стоп!'
                return message
        elif text.lower() == 'стоп':
            status_of_game.update({user_id: [0, 0]})
            message = 'Вы остановились на ' + str(score) + ' очках! \n'
            bot_score = randint(16, 24)
            if bot_score < score < 22:
                message += 'Победа! У вас ' + str(score) + ' очков, а у бота- ' + str(bot_score)
            elif score == bot_score:
                message += 'Ничья, у вас с ботом поровну очков!'
            elif score < bot_score < 22:
                message += 'Поражение! У вас ' + str(score) + ' очков, а у бота- ' + str(
                                     bot_score)
            else:
                message += 'Победа! У вас ' + str(score) + ' очков, а у бота- ' + str(bot_score)
            return message


def magic_ball():
    lst1 = {1: 'It is certain (Бесспорно)', 2: 'It is decidedly so (Предрешено)',
            3: 'Without a doubt (Никаких сомнений)',
            4: 'Yes — definitely (Определённо да)', 5: 'You may rely on it (Можешь быть уверен в этом)',
            6: 'As I see it, yes (Мне кажется — «да»)', 7: 'Most likely (Вероятнее всего)',
            8: 'Outlook good (Хорошие перспективы)', 9: 'Signs point to yes (Знаки говорят — «да»)',
            10: 'Yes (Да)', 11: 'Reply hazy, try again (Пока не ясно, попробуй снова)',
            12: 'Ask again later (Спроси позже)', 13: 'Better not tell you now (Лучше не рассказывать)',
            14: 'Cannot predict now (Сейчас нельзя предсказать)',
            15: 'Concentrate and ask again (Сконцентрируйся и спроси опять)',
            16: 'Don’t count on it (Даже не думай)', 17: 'My reply is no (Мой ответ — «нет»)',
            18: 'My sources say no (По моим данным — «нет»)',
            19: 'Outlook not so good (Перспективы не очень хорошие)', 20: 'Very doubtful (Весьма сомнительно)'}
    warn = 'Никогда не спрашивайте у меня о суициде! я вего лишь машина и работаю на рандоме! Я не несу' \
           ' ответственности за слова и советы, которые вам произношу!!!'

    result = randint(1, 21)
    print(result, lst1[result])
    return f"{warn}\n\n{lst1[result]}"


def rand(text):
    chisla = text.split()
    random = randint(int(chisla[1]), int(chisla[2]))
    return 'Вам выпало число:' + str(random)
