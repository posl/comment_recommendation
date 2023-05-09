def main():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i] == L[j] == L[k]:
                    ans += 1
                elif L[i] == L[j]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
                elif L[i] == L[k]:
                    if L[i] + L[k] > L[j]:
                        ans += 1
                elif L[j] == L[k]:
                    if L[j] + L[k] > L[i]:
                        ans += 1
                else:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)
