def main():
    N,M = map(int,input().split())
    S = []
    for _ in range(N):
        S.append(input())
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if 'o' in S[i] or 'o' in S[j]:
                count += 1
    print(count)
