#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import re
from functools import wraps

def get_duration(func):
    ''''Функция для подсчета затраченого времени'''

    @wraps(func)  # Декоратор @wraps сохраняет имя и описание декорированной функции
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)  # Вызов декорируемой функции
        end_time = time.perf_counter()
        res_time = end_time - start_time
        return res, res_time  # Добавить к результату функции время ее выполнения

    return wrapper
def valid_lst(text):
    '''Очищаем от лишнего'''
    if text == '':
        return []
    data_list = re.findall(r"[-+]?\d*\.?\d+", text)
    data_list = [float(num) if '.' in num else int(num) for num in data_list]
    return data_list

@get_duration
def bubble_sort(my_list):
    '''Сортировка пузырьком'''

    if len(my_list)<2:
        return output.insert(1.0, (my_list,'Тут нечего сортировать'))
    else:
        last_elem_index = len(my_list)-1
        for passNo in range(last_elem_index,0,-1):
            for idx in range(passNo):
                if my_list[idx]>my_list[idx+1]:
                    my_list[idx],my_list[idx+1]=my_list[idx+1],my_list[idx]
                    text1=my_list

    return my_list

@get_duration
def qsort(nums):
    '''Быстрая сортировка'''

    if len(nums)<2:
        return output.insert(1.0,(nums,'Тут нечего сортировать'))
    else:
        n = 1
        while n < len(nums):
           for i in range(len(nums) - n):
               if nums[i] > nums[i + 1]:
                   nums[i], nums[i + 1] = nums[i + 1], nums[i]
           n += 1

    return nums

@get_duration
def radix_sort(A):
    '''Поразрядная сортировка'''

    if len(A)<2:
        return output.insert(1.0, (A,'Тут нечего сортировать'))
    else:
        length = len(str(max(A)))
        rang = 10
        for i in range(length):
            B = [[] for k in range(rang)] #список длины range, состоящий из пустых списков
            for x in A:
                figure = int(x) // 10**i % 10
                B[figure].append(x)
            A = []
            for k in range(rang):
                A = A + B[k]
    return A

@get_duration
def mergesort(lst):
    '''Сортировка слиянием'''
    
    if len(lst)>1:
        mid = len(lst) // 2 # делим список пополам
        left = lst[:mid]
        right = lst[mid:]
        mergesort(left) # применяем функцию к левой и правой частям
        mergesort(right)
        a=0
        b=0
        c=0
        while a < len(left) and b < len (right):
            if left [a] < right [b]:
                lst[c] =left [a]
                a = a + 1
            else:
                lst [c] = right [b]
                b = b + 1
            c = c + 1
        while a < len(left):
            lst[c] = left[a]
            a = a + 1
            c = c + 1
        while b < len(right):
            lst[c] = right[b]
            b = b + 1
            c = c + 1
   
    return lst

def button_start():
    '''Функция, которую выполняет кнопка Поехали! - применяет сортировки'''
    second=[]
    second = valid_lst(entry_list.get())
    # first=entry_list.get()
    # second=[]
    # i = 0
    # while i < len(first):
    #     s_int = ''
    #     while i < len(first) and ('0' <= first[i] <= '9' or first[i] == '-'):
    #         s_int += first[i]
    #         i += 1
    #     i += 1
    #     if s_int != '':
    #         second.append((s_int))
    # for i in first:
    #     if i.isnumeric() :
    #         second.append(i)
    #print(first)
    print(second)
    method=combobox.get()
    print(method)
    
    if method == sort1:
        my_list=bubble_sort(second)
        return output.insert(1.0,("\nРезультат сортировки пузырьком и время выполнения:",my_list ))
    elif method ==sort2:
        nums=qsort(second)
        return output.insert(1.0,('\nРезультат быстрой сортировки и время выполнения:',nums ))
    elif method ==sort3:
        A=radix_sort(second)
        return output.insert(1.0,('\nРезультат поразрядной сортировки и время выполнения:',A ))
    elif method ==sort4:
        lst=mergesort(second)
        return output.insert(1.0,('\nРезультат сортировкой слияния и время выполнения:',lst ))
    else:
        return output.insert(1.0, text='Что-то не так, попробуйте ещё раз')
    #return output.insert(1.0, text='Сортировка выполнена!\nОчистийте поле перед следующим вводом')

def clear_output():
    '''Функция, которая очищает поле вывода'''
    output.delete(1.0,END)

#Создаем интерфейс
window=tk.Tk()
window.title("Добро пожаловать в сортировку чисел")
# Устанавливаем размер окна
window.geometry("900x900")
frame_top=Frame(window)
#frame_top=LabelFrame(window, text='Введите числа через запятую')
frame_top.pack()
frame_bot=Frame(window)
frame_bot.pack(fill=BOTH,expand=True,pady=5)

#Перечисляем типы возможной сортировки
sort1='Сортировка пузырьком'
sort2='Быстрая сортировка'
sort3='Поразрядная сортировка'
sort4='Сортировка слиянием'
sort_types=[sort1,sort2,sort3,sort4]
#по-умолчанию будет выбран первый элемент из sort_types
sort_var = StringVar(value=sort_types[0])

#Создаю подпись для поля ввода
first_label=Label(frame_top, text='Введите числа через запятую',font=("Arial", 16,"bold"))
first_label.pack(side=TOP)

#Создаем поле для ввода
entry_list=Entry(frame_top,width=100,text='enter',bd=2)
entry_list.focus_set()
entry_list.pack()

#Создаю подпись для выпадающего списка
second_label=Label(frame_bot, text='Выбирайте метод сортировки',font=("Arial", 16,"bold"))
second_label.pack(side=TOP)

#Выпадающий список
combobox = ttk.Combobox(frame_bot,textvariable=sort_var, values=sort_types)
combobox.pack(padx=6, pady=6)

#Создаем кнопку выполнения
button = Button(frame_bot, text = 'Поехали!', command=button_start)
button.pack(side = TOP, pady = 5)

#Кнопка очистки вывода
clr_button = Button(frame_bot, text = 'Очистить окно вывода', command=clear_output)
clr_button.pack(side = TOP, pady = 5)

#Создаем подпись и текстовое поле для вывода результата
third_label=Label(frame_bot, text='Результат работы программы:',font=("Arial", 16,"bold"))
third_label.pack()
output=Text(frame_bot,width=100, height=100, bd=2)
output.pack(side=BOTTOM)

#Тестирование
assert sort1=='Сортировка пузырьком'
assert sort2=='Быстрая сортировка'
assert sort3=='Поразрядная сортировка'
assert sort4=='Сортировка слиянием'
assert (bubble_sort([54,2,67,9])[0])==[2,9,54,67]
assert (qsort([54,2,67,9])[0])==[2,9,54,67]
assert (radix_sort([54,2,67,9])[0])==[2,9,54,67]
assert (mergesort([54,2,67,9])[0])==[2,9,54,67]
window.mainloop()


# In[ ]:




