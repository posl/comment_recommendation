def get_correct_answer(a,b):
    if a == 1 and b == 2:
        return 3
    elif a == 1 and b == 3:
        return 2
    elif a == 2 and b == 1:
        return 3
    elif a == 2 and b == 3:
        return 1
    elif a == 3 and b == 1:
        return 2
    elif a == 3 and b == 2:
        return 1

if __name__ == '__main__':
    get_correct_answer()