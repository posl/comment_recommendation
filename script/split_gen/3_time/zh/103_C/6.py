def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    max = 0
    for i in range(1, a[N-1]+a[N-2]+1):
        sum = 0
        for j in range(N):
            sum += i%a[j]
        if sum > max:
            max = sum
    print(max)
