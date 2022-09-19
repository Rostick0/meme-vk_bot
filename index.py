import random
import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

data = open('data.json', 'r')

memes = []

for i in data:
    memes.append(json.loads(i))

memes = memes[0]

token = 'vk1.a.aoR9p_KPaXSSxa5smoYjmf08HEd-wr3l9T7wOdgQqf5W3Spy--Mf_leI9c_0Cf9lB_E2FnXH-qRtBgmjGHyMQzMLC_540GcLL3YqKTbWOekp1557AlEdX8wtGDEJTTGZuzTNyCgEkRByvKWzcyTYMO38B_ejWz8JgHpeL2TG_ddCkbpzwv9Mni6NJ6i4jmUO'

bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


def blasthack(id, text, img = None, keyboard = None):
    message = {
                'user_id': id,
                'message': text,
                'random_id': 0
              }

    if (img):
        message['attachment'] = img

    if (keyboard):
        message['keyboard'] = keyboard.get_keyboard()

    bh.method('messages.send', message)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            message = event.text.lower()

            id = event.user_id

            keyboard = VkKeyboard()
            keyboard.add_location_button()

            buttons = ['мем']
            button_colors = [VkKeyboardColor.PRIMARY]

            keyboard.add_button(buttons[0], button_colors[0])

            if message == '/start' or message == 'начать':
                blasthack(id, 'Добро пожаловать, это тестовый бот, в котором вы можете просматривать мемы', None, keyboard)

            elif message == 'мем':
                mem = memes[random.randint(0, len(memes) - 1)]['meme']
                blasthack(id, None, mem)

            else:
                keyboard = VkKeyboard()
                keyboard.add_location_button()

                buttons = ['/start']
                button_colors = [VkKeyboardColor.PRIMARY]
                keyboard.add_button(buttons[0], button_colors[0])

                blasthack(id, 'Неизвестная команда, попробуйте нажать /start', None, keyboard)
