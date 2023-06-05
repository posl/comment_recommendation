def main():
    P = list(map(int, input().split()))
    alpha = [chr(i) for i in range(97, 123)]
    S = [alpha[i-1] for i in P]
    print(''.join(S))
