def main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 <= X:
        print(10**9)
        return
    ans = 0
    for i in range(1, 10):
        if A * 10**(i-1) + B * i <= X:
            ans = 10**(i-1)
        else:
            break
    if ans == 0:
        print(0)
        return
    for i in range(1, 10):
        if A * 10**(i-1) + B * i <= X:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()