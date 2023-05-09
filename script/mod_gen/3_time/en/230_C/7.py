def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    ans = []
    for i in range(P, Q+1):
        row = ""
        for j in range(R, S+1):
            if (i - j) % 2 == 0:
                if A <= i <= N - B + 1 and A <= j <= N - B + 1:
                    row += "#"
                else:
                    row += "."
            else:
                if A <= i <= N - B + 1 and B <= j <= N - A + 1:
                    row += "#"
                else:
                    row += "."
        ans.append(row)
    for row in ans:
        print(row)

if __name__ == '__main__':
    main()