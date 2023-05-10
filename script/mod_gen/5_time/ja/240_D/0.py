def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        a_i = a[i]
        if len(ans) == 0:
            ans.append(a_i)
            continue
        if ans[-1] == a_i:
            ans.pop()
        else:
            ans.append(a_i)
    print(len(ans))

if __name__ == '__main__':
    main()