def seven_multiple(K):
    i = 0
    s = 0
    while True:
        i += 1
        s = (s*10 + 7) % K
        if s == 0:
            return i
        if i == K:
            return -1
K = int(input())
print(seven_multiple(K))

if __name__ == '__main__':
    seven_multiple()