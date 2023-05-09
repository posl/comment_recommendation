def func(a):
    cnt = 0
    while True:
        for i in range(len(a)):
            if a[i] % 2 == 1:
                return cnt
        a = [i / 2 for i in a]
        cnt += 1

if __name__ == '__main__':
    func()