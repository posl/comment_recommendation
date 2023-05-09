def main():
    N = int(input())
    B = bin(N)[2:]
    B = B[::-1]
    B = B + "0" * (60 - len(B))
    B = B[::-1]
    for i in range(2 ** 15):
        S = bin(i)[2:]
        S = S[::-1]
        S = S + "0" * (15 - len(S))
        S = S[::-1]
        ans = 0
        for j in range(60):
            if S[j] == '1' and B[j] == '0':
                break
            if S[j] == '1':
                ans += 2 ** j
        else:
            print(ans)

if __name__ == '__main__':
    main()