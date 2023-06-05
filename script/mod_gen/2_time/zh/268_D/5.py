def main():
    n = int(input())
    ps = list(map(int, input().split()))
    ps = [p-1 for p in ps]
    # print(ps)
    cnt = 0
    for i in range(n):
        if ps[ps[ps[i]]] == i:
            cnt += 1
    print(cnt//2)

if __name__ == '__main__':
    main()