def main():
    N = input()
    ans = 0
    for i in range(len(N)):
        for j in range(len(N)):
            if i == j:
                continue
            x = int(N[:i+1])
            y = int(N[i+1:j+1])
            if x == 0 or y == 0:
                continue
            ans = max(ans, x*y)
    print(ans)

if __name__ == '__main__':
    main()