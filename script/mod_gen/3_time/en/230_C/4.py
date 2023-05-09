def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        ans = ""
        for j in range(R, S + 1):
            if (i + j) % 2 == 0:
                ans += "#"
            else:
                ans += "."
        print(ans)

if __name__ == '__main__':
    main()