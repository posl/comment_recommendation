def main():
    a, n = map(int, input().split())
    x = 1
    for i in range(1, 10**6):
        x = int(str(x)[-1] + str(x*a)[0])
        if x == n:
            print(i)
            return
    print(-1)
    return
