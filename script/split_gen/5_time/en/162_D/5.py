def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    total = R * G * B
    for i in range(1, N):
        for j in range(N):
            k = j + i
            if k >= N:
                break
            if S[j] != S[k]:
                if S[j] != S[i + k]:
                    if S[i + k] != S[k]:
                        total -= 1
    print(total)
