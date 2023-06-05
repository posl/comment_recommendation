def check_winner(a, b):
    if a == 'G' and b == 'C':
        return True
    elif a == 'C' and b == 'P':
        return True
    elif a == 'P' and b == 'G':
        return True
    else:
        return False

if __name__ == '__main__':
    check_winner()