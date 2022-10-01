# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))