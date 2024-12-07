# TODO  Напишите функцию count_letters

def count_letters(low_ver):
    letter_counter = {} # словарь для подсчета букв
    low_ver = low_ver.lower() # Перевод буквенных значений в строчную версию

    for letter in low_ver:
        if letter.isalpha(): # Условие для проверки буквенных символов
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 1

    return letter_counter
# TODO Напишите функцию calculate_frequency

def calculate_frequency(letter_counter):
    frequency = {}
    letter_calculation = sum(letter_counter.values())

    for letter, count in letter_counter.items():
        frequency[letter] = count / letter_calculation

    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_counter = count_letters(main_str)
frequency = calculate_frequency(letter_counter)
# TODO Распечатайте в столбик букву и её частоту в тексте

for letter, count in frequency.items():
    print(f"{letter}: {count:.2f}")
