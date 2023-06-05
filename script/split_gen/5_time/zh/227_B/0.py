def main():
    # N = int(input())
    # S = list(map(int, input().split()))
    N = 5
    S = [666, 777, 888, 777, 666]
    error = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                error += 1
    print(error)
