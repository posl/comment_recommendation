def func(a, b, k):
    cnt = 0
    while True:
        if a >= b:
            break
        a *= k
        cnt += 1
    return cnt

if __name__ == '__main__':
    func()