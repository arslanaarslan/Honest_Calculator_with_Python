msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

op = ['+', '-', '/', '*']
memory = float(0)


def is_digit(msg):
    if is_float(msg):  # integer numbers are checked as well so no need to add another control for checking int
        return True
    else:
        return False


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calculate(operation):
    global result
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        if y != 0:
            result = x / y
        else:
            result = msg_3
    return result


def check_func():
    store_data()
    if not continue_calc():
        return False
    else:
        return True


def print_message(index):
    if index == 10:
        print(msg_10)
    elif index == 11:
        print(msg_11)
    elif index == 12:
        print(msg_12)


def store_data():
    global memory
    print(msg_4)
    input_msg = input()

    if input_msg == 'y':
        if is_one_digit(result):
            msg_index = 10
            while True:
                print_message(msg_index)
                input_msg = input()
                if input_msg == 'y':
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        break
                elif input_msg == 'n':
                    break
        if input_msg != 'n':
            memory = result
    elif input_msg != 'y' and input_msg != 'n':
        check_func()


def continue_calc():
    print(msg_5)
    input_msg = input()

    if input_msg == 'n':
        return False
    elif input_msg != 'y':
        check_func()
    return True


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6

    if ((is_digit(v1) and (float(v1) == 1)) or (is_digit(v2) and (float(v2) == 1))) and v3 == '*':
        msg = msg + msg_7

    if ((is_digit(v1) and (float(v1) == 0)) or (is_digit(v2) and (float(v2) == 0))) and (
            v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8

    if msg != '':
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


while True:
    print(msg_0)
    rcv_msg = input().split(" ")

    if rcv_msg[0] == 'M':
        rcv_msg[0] = str(memory)
    if rcv_msg[2] == 'M':
        rcv_msg[2] = str(memory)

    if not (is_digit(rcv_msg[0]) and is_digit(rcv_msg[2])):
        print(msg_1)
    elif not rcv_msg[1] in op:
        print(msg_2)
    else:
        x = float(rcv_msg[0])
        y = float(rcv_msg[2])

        check(x, y, rcv_msg[1])

        result = calculate(rcv_msg[1])
        print(result)

        if result != msg_3 and not check_func():
            break
