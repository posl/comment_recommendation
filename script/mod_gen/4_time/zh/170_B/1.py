def is_answer(x, y):
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            return True
    return False

if __name__ == '__main__':
    is_answer()