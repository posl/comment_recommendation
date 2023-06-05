def game(a, b):
    if a == b:
        return 0
    elif a == 'G' and b == 'C':
        return 1
    elif a == 'C' and b == 'P':
        return 1
    elif a == 'P' and b == 'G':
        return 1
    else:
        return -1

if __name__ == '__main__':
    game()