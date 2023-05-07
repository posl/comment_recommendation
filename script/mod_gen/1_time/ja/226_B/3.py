def main():
    N = int(input())
    dict = {}
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] in dict:
            dict[L[0]].append(L[1:])
        else:
            dict[L[0]] = [L[1:]]
    ans = 0
    for key in dict:
        ans += len(set([tuple(v) for v in dict[key]]))
    print(ans)

if __name__ == '__main__':
    main()