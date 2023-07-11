# task 1

numOne = input("введіть число 1")
numTwo = input("введіть число 2")
numThree = input("введіть число 3")
print(numOne+numTwo+numThree)

# task 2

a = int(input("введіть число "))
b = int(input("введіть число "))
c = int(input("введіть число "))
d = int(input("введіть число "))
print(a*b*c*d)

# task 3

metres = int(input("Введіть кількість метрів"))
if metres < 0:
    print("метри не можуть бути від'ємним значенням, введіть ще раз")
    pass

if metres == 0:
    print("значення не може дрівнювати нулю, введіть ще раз")
    pass

centimetre = metres * 100
decimetre = metres * 10
miles = metres * 0.00062137119609836
miles = round(miles, 3)
milimetres = metres * 1000
print("отож,", metres, "метрів - це є", centimetre, "сантиметрів", decimetre, "дециметрів", milimetres, "міліметрів", miles, "миль")

# task 4

side_a = int(input("Введіть довжину сторони а"))
height_a = int(input("введіть довжину висоти від сторони а "))
print(0.5 * side_a * height_a)

number = int(input("Введіть число: "))
reversed_number = 0

while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

print("Результат:", reversed_number)
