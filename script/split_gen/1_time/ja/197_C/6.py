def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        #print(i)
        zero = 0
        one = 0
        for j in range(N):
            if A[j] & (1 << i):
                one += 1
            else:
                zero += 1
        #print(zero, one)
        ans += (one * zero) * (1 << i)
        #print(ans)
    print(ans)
