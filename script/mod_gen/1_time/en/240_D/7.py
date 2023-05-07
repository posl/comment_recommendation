def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        a_i = a[i]
        if a_i % 2 == 0:
            ans.append(1)
        else:
            ans.append(0)
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()