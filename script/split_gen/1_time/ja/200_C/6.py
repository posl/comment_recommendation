def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]
    #print(A)
    d = dict()
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    #print(d)
    ans = 0
    for k in d:
        ans += d[k]*(d[k]-1)//2
    print(ans)
