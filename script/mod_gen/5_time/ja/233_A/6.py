def main():
    X,Y = map(int, input().split())
    ans = 0
    if X >= Y:
        ans = 0
    else:
        ans = Y // 10 - X // 10
        if Y % 10 == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()