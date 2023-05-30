def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 3
    a = [1000000000, 1000000000, 1000000000]
    a.sort()
    while True:
        if len(a) == 1:
            break
        if a[-1] == a[-2]:
            a[-2] = a[-1] = a[-1] // 2
            a.sort()
        else:
            a[-1] = a[-1] - a[-2]
            a.sort()
    print(a[0])
main()
