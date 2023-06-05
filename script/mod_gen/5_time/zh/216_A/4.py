def print_grade(x, y):
    if y <= 2:
        print(x + "-")
    elif y <= 6:
        print(x)
    else:
        print(x + "+")

if __name__ == '__main__':
    print_grade()