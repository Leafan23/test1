'''
На входе список чисел. Вернуть True, если массив содержит где-нибудь 3 рядом с 3
Пример результата функции:
has_33 ([1, 3, 3])  ---> True
has_33 ([3, 1, 3, 1]) ---> False
'''


def check_33(nums):
    count = 0
    user_array = list(nums)
    for i in range(len(user_array) - 1):
        if user_array[count] == 3 == user_array[count + 1]:
            return True
        else:
            count += 1
    return False
#Бля заебал

x = 1, 2, 3, 4, 5, 1, 3, 7, 3, 3, 5, 7

y = 21, 21, 32

print(check_33(x))

"""
На входе строка, вернуть строку где каждый символ исходной строки
 повторяется три раза
"""


def multiplite_me(user_string):
    """ get the string from user and return it,
     but multiplying each letter by 3   """
    result_string = []
    count = 0
    for i in range(len(user_string)):
        result_string.append(user_string[count] * 3)
        count += 1
    return ''.join(result_string)


print(multiplite_me('abcdefg'))

'''
Лучшее решение:
def better_that_u(text):
    result = ''
    for char in text:
        result += char * 3
    return result

'''

'''
Блекджек: На входе 3 числа от 1 до 11. Если их сумма меньше илиравна 21,
то вернуть их сумму. Если сумма больше 21 и среди чисел есть 11, то уменьшить
общую сумму на 10. Инаконец, если сумма (в том числе после уменьшения)
превышает 21, вернуть 'bust'
'''


def blackjack(card1, card2, card3):
    if card1 > 11 or card2 > 11 or card3 > 11:
        return 'no no no señor!'
    else:
        cardsum = card1 + card2 + card3
        if cardsum <= 21:
            return cardsum
        else:
            if card1 == 11 or card2 == 11 or card3 == 11:
                cardsum = cardsum - 10
                if cardsum < 21:
                    return cardsum
            else:
                return 'Потрачено'


print(blackjack(8, 8, 11))

'''
Лучшее решение:
def blackjack(card1, card2, card3):
    if sum([card1, card2, card3]) <= 21:
        return sum([card1, card2, card3])
    elif 11 in [card1, card2, card3] and sum([card1, card2, card3]) - 10 <= 21:
        return sum([card1, card2, card3]) - 10
    else:
        return 'Bust'

Кстати хз почему у него нет прроверки того, нет ли на входе числа больше 11
'''

