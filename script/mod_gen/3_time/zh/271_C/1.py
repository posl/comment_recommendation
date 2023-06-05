def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i, j in enumerate(a):
        if i+1 < j:
            ans = i+1
    print(ans)

if __name__ == '__main__':
    main()