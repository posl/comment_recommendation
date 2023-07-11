def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R * G * B
    for i in range(N):
        for j in range(i+1,N):
            k = 2 * j - i
            if k >= N:
                continue
