first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first==second==third:
    print("Три")
elif first==second or first==third or second==third:
    print("Два")
else:
    print("Ноль")