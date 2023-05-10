def snuke_number(k):
    i = 1
    while True:
        if i % sum(map(int, str(i))) == 0:
            k -= 1
            if k == 0:
                return i
        i += 1

if __name__ == '__main__':
    snuke_number()