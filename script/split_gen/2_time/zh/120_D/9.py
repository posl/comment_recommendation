def main():
    S = input()
    N = len(S)
    num = 0
    for i in range(N):
        if S[i] == '1':
            num += 1
    print(min(num, N-num)*2)
