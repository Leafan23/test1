'''
Напишите функцию, которая возвращает меньшее из двух чисел, если оба этих числа
 чётные. Если хоть одно число нечетное, возвращает большее из двух чисел
'''


def lesser_of_two_evens(num1, num2):
    # Пишем прелесную конструкцию из ифов. Её логика совершенна.
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
    else:
        if num1 > num2:
            return num1
        else:
            return num2
# другое решение:

def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)












"""Напишите функцию, которая получает на входе строку из двух слов,
и возвращает True, если оба слова начинаются с одной буквы """


def two_words(text):
  bothwords = text.split()
  return bothwords[0][0] == bothwords[0][1]

print(two_words('hgfhgfh hfghg'))
"""
На входе 2 числа. Функция возвращает True, если сумма этих чисел равна 21
"""


def black_jack(card1, card2):
    if card1 + card2 == 21:
        print('BlackJack!')
        return True
    else:
        print('nope')
        return False


x = black_jack(11, 10)

"""Напишите функцию, которая переводит в верхний регистр первую и четрвёртую
буквы слова. Исправьте macdonald в MacDonald """


def capitalize_me(word):
    # divide the word into 2 parts and write each with a capital letter
    print(word[:3].capitalize() + word[3:].capitalize())


macdonald = 'macdonald'
capitalize_me(macdonald)

"""
На входе фраза, на выходе вернуть слова в обратном порядке.
Пригодится метод .join  Пример:
Код '+'.join('a', 'b', 'c') позволит получить строку:
'a+b+c'
"""


def the_string(user_string):
    splitted_string = user_string.split(' ')
    new_string = splitted_string[::-1]
    final_string = ' '.join(new_string)
    return final_string


z = 'uno dos tres'
print(the_string(z))


def capitalize_me(word):
    print(word[:3].capitalize() + word[3:].capitalize())