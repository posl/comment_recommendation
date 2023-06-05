def get_score(a,b):
    if a == b:
        return a + b
    elif a > b:
        return a + b + 1
    else:
        return a + b + 1

if __name__ == '__main__':
    get_score()