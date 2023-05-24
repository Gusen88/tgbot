from ques import numbers, right_answer, questions,answers
import random
from aiogram import Bot, Dispatcher, executor, types

def PyBot():
    # Инициализация бота
    bot = Bot(token='6201566377:AAHcH8VE8PEdITynui-yc--vL1o-8SWYXyY')
    dp = Dispatcher(bot)
    file = []

    @dp.message_handler(commands=['start'])
    async def start_game(message:types.Message):
        global right_answers,count
        count = 1
        right_answers = 0
        random.shuffle(numbers)
        await message.answer(f'Вопрос {count}: {questions[numbers[count-1]]}')
        await message.answer(f'{answers[numbers[count-1]]}')
        await message.answer(f'Введите ответ')
        count += 1

    @dp.message_handler()
    async def users_answer(message:types.Message):
        global count,right_answers
        if count <= len(numbers):
            if message.text == right_answer[numbers[count-2]]:
                global right_answers
                right_answers += 1
                await message.answer(f'Правильно! Продолжаем!\nПравильных ответов {right_answers} из {count-1}')
            else:
                await message.answer(f'Неправильно :( Правильный ответ : {right_answer[numbers[count-2]]}. Продолжаем!\nПравильных ответов {right_answers} из {count-1}')
            await message.answer(f'Вопрос {count}: {questions[numbers[count - 1]]}')
            await message.answer(f'{answers[numbers[count - 1]]}')
            await message.answer(f'Введите ответ')
            count += 1
        else:
            if message.text == right_answer[numbers[count-2]]:
                right_answers += 1
                await message.answer(f'Правильно!')
            else:
                await message.answer(f'Неправильно :( Правильный ответ : {right_answer[numbers[count-2]]}.')
            await message.answer(f'Игра завершена!')
            if right_answers == count-1:
                await message.answer(f'Вы победили!\nПравильных ответов {right_answers} из {count-1}')
            else:
                await message.answer(f'К сожалению, вы проиграли. Повезёт в следующий раз!\nПравильных ответов {right_answers} из {count-1}')
    executor.start_polling(dp, skip_updates=True)