def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, t)
    # print(a)
    # t = t - 1
    # t = t % sum(a)
    # print(t)
    # for i in range(n):
    #     if t < a[i]:
    #         print(i+1, t)
    #         break
    #     t -= a[i]
    # print(a)
    t -= 1
    t %= sum(a)
    # print(t)
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]
