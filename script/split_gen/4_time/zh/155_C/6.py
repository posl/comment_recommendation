def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max_count = 0
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            count = 0
        if
