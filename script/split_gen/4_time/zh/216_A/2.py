def print_sign_of_x(x):
    if 0 <= x <= 2:
        print(str(x) + "-")
    elif 3 <= x <= 6:
        print(str(x))
    elif 7 <= x <= 9:
        print(str(x) + "+")
    else:
        print("error")
