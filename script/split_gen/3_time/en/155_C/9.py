def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S.append('')
    count = 0
    for i in range(N):
        if S[i] == S[i+1]:
            count += 1
        else:
            if count == N-1:
                print(S[i])
            count = 0
