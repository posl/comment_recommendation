def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if D >= (x**2+y**2)**(1/2):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()