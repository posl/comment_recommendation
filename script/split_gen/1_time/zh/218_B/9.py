def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + P[i] - 1) for i in range(26)]
    print(''.join(S))
