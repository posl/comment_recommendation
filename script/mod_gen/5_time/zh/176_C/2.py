def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    ans = 0
    for a in A:
        if a >= ans:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()