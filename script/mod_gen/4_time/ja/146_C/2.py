def main():
    a,b,x = map(int, input().split())
    ans = 0
    if a * 10 + b * 1 <= x:
        ans = 10
    elif a * 1 + b * 1 <= x:
        ans = 1
    else:
        ans = 0
    print(ans)

if __name__ == '__main__':
    main()