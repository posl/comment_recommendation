def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    l = [0]
    for a in A:
        l.append(l[-1] + a)
    ans = 10**18
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                ans = min(ans, max(l[i], l[j]-l[i], l[k]-l[j], s-l[k]) - min(l[i], l[j]-l[i], l[k]-l[j], s-l[k]))
    print(ans)
