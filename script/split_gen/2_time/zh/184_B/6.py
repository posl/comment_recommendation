def main():
    N, X = map(int, input().split())
    S = input()
    sum = X
    for i in range(N):
        if S[i] == 'o':
            sum += 1
        else:
            if sum > 0:
                sum -= 1
    print(sum)
