def main():
    N = int(input())
    S = input()
    R = 0
    G = 0
    B = 0
    for s in S:
        if s == "R":
            R += 1
        elif s == "G":
            G += 1
        else:
            B += 1
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] != S[j]:
                if i + (j - i) * 2 < N:
                    if S[i] != S[i + (j - i) * 2] and S[j] != S[i + (j - i) * 2]:
                        ans -= 1
                if i - (j - i) >= 0:
                    if S[i] != S[i - (j - i)] and S[j] != S[i - (j - i)]:
                        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()