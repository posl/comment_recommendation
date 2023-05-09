def main():
    N = int(input())
    S = input()
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == "R":
            R += 1
        elif S[i] == "G":
            G += 1
        else:
            B += 1
    ans = R * G * B
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            k = 2 * j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans -= 1
    print(ans)

if __name__ == '__main__':
    main()