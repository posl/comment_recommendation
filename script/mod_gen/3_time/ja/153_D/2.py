def calc(h):
    if h == 1:
        return 1
    else:
        return 2 * calc(h//2) + 1
h = int(input())
print(calc(h))

if __name__ == '__main__':
    calc()