def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            count += 1
    print(count)
