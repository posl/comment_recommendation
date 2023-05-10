def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    pos = 0
    for a in A:
        pos += a
        ans = max(ans, pos)
    print(ans)
main()

if __name__ == '__main__':
    main()