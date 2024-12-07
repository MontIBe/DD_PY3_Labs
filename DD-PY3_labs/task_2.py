# TODO Напишите функцию find_common_participants

def find_common_participants(group_1, group_2, separate = ','):
    K_group_1 = group_1.split(separate)
    K_group_2 = group_2.split(separate)

    list_name = list(set(K_group_1).intersection(K_group_2))
    list_name.sort()

    return list_name
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))