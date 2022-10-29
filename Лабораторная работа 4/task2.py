def get_count_char(str_):
    str_ = "".join(str_.split())
    str_ = str_.lower()
    alfa = {}
    for elf in str_:
        if elf.isalpha():
          if elf in alfa:
            alfa[elf] += 1

          else:
            alfa[elf] = 1

    return alfa

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))