ticket = input("Введите номер билета:")

if len(ticket) !=6 or not ticket.isdigit():
    print("Ошибка! Введите ровно 6 цифр")
else:
    digite = [int(digite) for digite in ticket]

    if sum(digite[:3]) == sum(digite[:3]):
        print("Счасливый")
    else:
        print("Обычный")