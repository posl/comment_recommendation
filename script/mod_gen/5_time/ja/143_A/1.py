def main():
    a, b = map(int, input().split())
    ans = a - b * 2
    if ans < 0:
        ans = 0
    print(ans)

if __name__ == '__main__':
    main()