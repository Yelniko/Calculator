import re


class Format:
    def __int__(self, number, dictionary):
        self.number = number
        self.dictionary = dictionary

    def verification(self, number):
        """ Перевірка елементу на валідність  """
        return re.fullmatch(self.dictionary, number) is not None

    def translation_10(self, number, glossary='0123456789ABCDEF'):
        number = number.split('.')
        number[0] = list(reversed(number[0]))
        suma = 0
        for i in range(0, len(number[0])):
            suma += glossary.index(number[0][i]) * self.number ** i
        if len(number) != 1:
            number[1] = list(number[1])
            for i in range(0, len(number[1])):
                suma += glossary.index(number[1][i]) * self.number ** ((i+1) * -1)
        return str(suma)

    def translation(self, number, glossary='0123456789ABCDEF'):
        number = number.split('.')
        lis = ['', int(number[0])]
        while lis[1] != 0:
            lis[0] = glossary[(lis[1] % self.number)] + lis[0]
            lis[1] //= self.number
        if len(number) != 1:
            lis = [lis[0]+'.', float('0.'+number[1])]
            for i in range(0, 9):
                lis[0] = lis[0] + glossary[int(lis[1]*self.number)]
                lis[1] = float((lis[1]*self.number) % 1)
                if lis[1] == 0:
                    break
        return str(lis[0])


class BIN(Format):
    """ Клас для оброблення 2 системи числення """
    number = 2
    dictionary = r'(^[0-1]+$)'
    disabled = [True, False, False, False, False,
                True, False, False, False, False,
                True, True, True, True, False,
                True, True, True, True, False,
                True, False, True, True, False,
                True, False, False, False, False, ]

    def __int__(self, number, dictionary):
        super().__init__()


class OCT(Format):
    """ Клас для оброблення 8 системи числення """
    number = 8
    dictionary = r'(^[0-7]+$)'
    disabled = [True, False, False, False, False,
                True, False, False, False, False,
                True, False, True, True, False,
                True, False, False, False, False,
                True, False, False, False, False,
                True, False, False, False, False, ]

    def __int__(self, number, dictionary):
        super().__init__()


class DEC(Format):
    """Клас для оброблення 10 системи числення"""

    number = 10
    dictionary = r'(^[0-9]+$)'
    disabled = [True, False, False, False, False,
                True, False, False, False, False,
                True, False, False, False, False,
                True, False, False, False, False,
                True, False, False, False, False,
                True, False, False, False, False, ]

    def __int__(self, number, dictionary):
        super().__init__()


class HEX(Format):
    """Клас для оброблення 16 системи числення"""
    number = 16
    dictionary = r'(^[0-9A-Fa-f]+$)'
    disabled = [False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False, ]

    def __int__(self, number, dictionary):
        super().__init__()
