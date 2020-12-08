def start_s():
    my_line = 'Print only the words that start with an s in this sentence'
    words_in_my_line = my_line.split(" ")

    first_letter = 's'

    for word in words_in_my_line:
        if word[0] == first_letter:
            print(word)


def even_numbers():
    for i in range(0, 11):
        if i % 2 == 0:
            print(i)


def devided_three():
    #listdevided = [i for i in range(1, 51) if i % 3 == 0]

    print(i for i in range(1, 51) if i % 3 == 0)


def even_words():
    my_line2 = 'Print every word in this sentence that has an even number of letters'
    words_in_my_line2 = my_line2.split(" ")
    x = 0
    for i in words_in_my_line2:
        if len(words_in_my_line2[x]) % 2 == 0:
            print('This word has an even number of words: ', words_in_my_line2[x])
        x += 1


def fizz_buzz():
    for count in range(1, 30):
        if count % 5 == 0 and count % 3 == 0:
            print('FizzBuzz')
        elif count % 3 == 0:
            print('Fizz')
        elif count % 5 == 0:
            print('Buzz')
        else:
            print(count)











