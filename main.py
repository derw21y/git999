if __name__ == '__main__':
    words = []
    xb = 'Стоп'
    wrd = ()
    while wrd != xb:
        if wrd != xb:
            wrd = input('Введите новое слово ')
            words.append(wrd)
    words.remove('Стоп')
    print(words)