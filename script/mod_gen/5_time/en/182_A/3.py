def max_follow(a,b):
    if a <= 2*b + 100:
        return 2*b + 100 - a
    else:
        return 0

if __name__ == '__main__':
    max_follow()