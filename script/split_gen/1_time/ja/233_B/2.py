def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = S[L-1:R][::-1]
    print(''.join(S))
