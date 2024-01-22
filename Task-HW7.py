"""
Напишіть функцію, яка обчислює добуток елементів списку цілих.
Список передається як параметр. Отриманий результат повертається із функції.
"""

# def calc_product(num_list):
#     product = 1
#     for num in num_list:
#         product *= num
#     return product
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 22, 35, 40]
#
# result = calc_product(num_list)
#
# print(f"Calculated product: {num_list}: {result}")


"""
Напишіть функцію для знаходження мінімуму у списку цілих. 
Список передається як параметр. Отриманий результат повертається із функції.
"""

# def find_min(num_list):
#     if not num_list:
#         return None
#
#     min = num_list[0]
#
#     for num in num_list:
#         if num < min:
#             min = num
#     return min
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = find_min(num_list)
# print(f"minimum result in list {num_list}: {result}")


"""
Напишіть функцію, яка визначає кількість простих чисел у списку цілих. 
Список передається як параметр. Отриманий результат повертається із функції.
"""

# Визначаємо чи є число постим
# def is_prime_number(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# Визначаємо кількість простих чисел
# def count_prime_numbers(num_list):
#     count = 0
#     for num in num_list:
#         if is_prime_number(num):
#             count += 1
#     return count

# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = count_prime_numbers(num_list)
# print(f"The number of primes in the list {num_list}: {result}")


"""
Напишіть функцію, яка видаляє зі списку ціле задане число.
З функції потрібно повернути кількість видаленних елементів.
"""

# def remove_from_list(input_list, number):
#     number_for_deletion = input_list.count(number)
#     input_list = [num for num in input_list if num != number]
#     return number_for_deletion, input_list
#
# num_list = [1, 2, 3, 4, 2, 5, 6, 7, 2, 8, 9]
# number_for_deletion = 2
#
# number_removed, num_list = remove_from_list(num_list, number_for_deletion)
# print(f"Items removed {number_for_deletion} from the list: {num_list}")


"""
Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
"""

# def merge_lists(list1, list2):
#     return list1 + list2
#
# list1 = [1, 2, 3]
# list2 = [5, 6, 7]
#
# linked_lists = merge_lists(list1, list2)
# print("Linked lists:", "Merged lists:", linked_lists)


"""
Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. 
Значення для ступеня передається як параметр, список також передається як параметр. 
Функція повертає новий список, який містить отримані результати.
"""

def calculate_degree_of_list(numbers, degree):
    return [num ** degree for num in numbers]

numbers_list = [1, 2, 3, 4, 5]
degree_value = 3

result = calculate_degree_of_list(numbers_list, degree_value)
print(f"Result of raising to the power {degree_value}: {result}")