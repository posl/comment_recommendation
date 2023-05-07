def main():
    S = input()
    N = len(S)
    count = [0] * N
    for i in range(N):
        if S[i] == 'R':
            count[i] += 1
        else:
            count[i-1] += 1
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            count[i] += 1
        else:
            count[i+1] += 1
    print(' '.join(map(str, count)))
