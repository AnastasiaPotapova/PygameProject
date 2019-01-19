class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


def check_len(password):
    if len(password) <= 8:
        raise LengthError


def check_let(password):
    if password == password.lower() or password == password.upper():
        raise LetterError


def check_dig(password):
    x = [d in '1234567890' for d in list(password)]

    if not (True in x and False in x):
        raise DigitError


def check_seq(password):
    for i in range(len(password) - 2):
        if password[i:i + 3].lower() in 'qwertyuiop':
            raise SequenceError
        elif password[i:i + 3].lower() in 'asdfghjkl':
            raise SequenceError
        elif password[i:i + 3].lower() in 'zxcvbnm':
            raise SequenceError
        elif password[i:i + 3].lower() in 'йцукенгшщзхъ':
            raise SequenceError
        elif password[i:i + 3].lower() in 'фывапролджэё':
            raise SequenceError
        elif password[i:i + 3].lower() in 'ячсмитьбю':
            raise SequenceError


def check_word(password):
    data = open("top-9999-words.txt").read().split()
    if password in data:
        raise WordError


spisok = open("top 10000 passwd.txt").read().split()
LenE = 0
LetE = 0
DigE = 0
SeqE = 0
WorE = 0
for i in spisok:
    try:
        check_len(i)
    except LengthError:
        LenE += 1
    try:
        check_let(i)
    except LetterError:
        LetE += 1
    try:
        check_dig(i)
    except DigitError:
        DigE += 1
    try:
        check_seq(i)
    except SequenceError:
        SeqE += 1
    try:
        check_word(i)
    except WordError:
        WorE += 1
print('DigitError - ' + str(DigE))
print('LengthError - ' + str(LenE))
print('LetterError - ' + str(LetE))
print('SequenceError - ' + str(SeqE))
print('WordError - ' + str(WorE))
