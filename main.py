#if __name__ == "__main__":
    # task 1

    # a = int(input("Введіть перше число потрібного вам діапазону"))
    # b = int(input("Введіть друге число потрібного вам діапазону"))+ 1
    # for i in range(a, b, 1):
    #     if i%7 == 0:
    #         print(i)

    # task 2

    # diapazon_start = int(input("Введіть перше число потрібного вам діапазону"))
    # diapazon_end = int(input("Введіть перше число потрібного вам діапазону"))+1
    # reversed_numbers = []
    # numbers_for_five = []
    # numbers_for_seven = []
    # numbers_task_two = []
    # for i in range(diapazon_start, diapazon_end, 1):
    #     reversed_numbers.append(i)
    #     numbers_task_two.append(i)
    #     if i%5 == 0:
    #         numbers_for_five.append(i)
    #     if i%7 == 0:
    #         numbers_for_seven.append(i)
    #
    #
    # reversed_numbers.sort(reverse=True)
    # print(numbers_task_two, "усі числа в діапазоні")
    # print(reversed_numbers, "у порядку спадання")
    # print(len(numbers_for_five)+ 1, "кількість кратних 5")
    # print(numbers_for_seven, "кратні 7")


    # task 3

    number_one = int(input("Введіть перше число потрібного вам діапазону"))
    number_two = int(input("Введіть друге число потрібного вам діапазону"))+1
    for i in range(number_one, number_two, 1):
        if i%3 ==0 and i%5 == 0:
            print("Fizz Buzz")
        elif  i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)




