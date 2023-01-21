
# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

numbers = [random.randint(1,10) for i in range(6)]
print(numbers)

result = lambda x: x > 5
result = list(filter(result, numbers))
print(result)

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random

numbers = [random.randint(1, 10) for i in range(8)]
print(numbers)
result = [numbers[0]]
for el in numbers:
     if el > result[-1]:
         result.append(el)
print(result)

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random
rnd = random.randint(1, 87)
numbers = [random.randint(1, 10) for i in range(rnd)]
print(numbers)

print('Список элементов:')
non_repeat_numbers = list(filter(lambda x: numbers.count(x) == 1, numbers))
print(non_repeat_numbers)

count = len(numbers) - len(non_repeat_numbers)
print('Cовпадает элементов: ', count)


# Задача 4*. Создайте игру в крестики-нолики.


print("*" * 10, " Игра в крестики-нолики ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
     print("-" * 13)
     for i in range(3):
         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
         print("-" * 13)

def take_input(player_token):
     valid = False
     while not valid:
         player_answer = input("Куда поставим " + player_token+"? ")
         try:
             player_answer = int(player_answer)
         except:
             print("Вы уверены, что ввели число?")
             continue
         if player_answer >= 1 and player_answer <= 9:
             if(str(board[player_answer-1]) not in "XO"):
                 board[player_answer-1] = player_token
                 valid = True
             else:
                 print("Эта клетка уже занята")
         else:
             print("Введите число от 1 до 9")

def check_win(board):
     win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
     for each in win_coord:
         if board[each[0]] == board[each[1]] == board[each[2]]:
             return board[each[0]]
     return False

def main(board):
     counter = 0
     win = False
     while not win:
         draw_board(board)
         if counter % 2 == 0:
             take_input("X")
         else:
             take_input("O")
         counter += 1
         if counter > 4:
             tmp = check_win(board)
             if tmp:
                 print(tmp, "Победа")
                 win = True
                 break
         if counter == 9:
             print("Ничья")
             break
     draw_board(board)
main(board)

input("Нажмите Enter для выхода")