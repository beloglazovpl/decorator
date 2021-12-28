from cook_book.cook_book import get_shop_list_by_dishes


dishes = ['Борщ', 'Запеченный картофель', 'Утка по-пекински']
person = 3

if __name__ == "__main__":
     get_shop_list_by_dishes(dishes, person)
     print(f'Ингредиенты для блюд: {", ".join(str(dish) for dish in dishes)} на {person} гостя(ей) расчитаны')
