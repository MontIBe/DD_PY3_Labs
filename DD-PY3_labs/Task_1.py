# TODO Напишите функцию для поиска индекса товара

def search_product(product_list, desired_product):
    if desired_product in product_list: # Условие для продукта в списке
        return product_list.index(desired_product) # Возврат индекса искомого продукта в списке

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_product(items_list, find_item) # Функция для получения индекса товара

    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
