def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if S[i] == 1:
            count += 1
        else:
            for j in range(2, S[i]//2):
                if S[i] % j == 0:
                    count += 1
                    break
    print(N-count)
