def main():
    S = input()
    N = len(S)
    R = 2019
    C = [0] * R
    C[0] = 1
    ans = 0
    d = 1
    for s in S[::-1]:
        ans += C[int(s) * d % R]
        C[int(s) * d % R] += 1
        d = d * 10 % R
    print(ans)

if __name__ == '__main__':
    main()