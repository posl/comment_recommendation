def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N+1)
    a.insert(0,0)
    a = [a[i] - a[i-1] - 1 for i in range(1,M+2)]
    a = list(filter(lambda x: x>0, a))
    if len(a) == 1:
        print(1)
        return
    a.sort()
    min_a = a[0]
    a = [i//min_a for i in a]
    a = [i-1 for i in a]
    #print(a)
    #print(min_a)
    ans = 1
    for i in a:
        ans *= i
        ans %= 10**9+7
    print(ans)
