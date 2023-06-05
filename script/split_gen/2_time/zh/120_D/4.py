def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N):
        if S[i] == '1':
            count += 1
    print(min(count, N - count) * 2)
