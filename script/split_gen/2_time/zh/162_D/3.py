def main():
    N = input()
    S = raw_input()
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == 'R':
            R += 1
        if S[i] == 'G':
            G += 1
        if S[i] == 'B':
            B += 1
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k < N and S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print ans
