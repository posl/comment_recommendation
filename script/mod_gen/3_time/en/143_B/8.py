def takoyaki_festival():
    N = int(input())
    d = list(map(int, input().split()))
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            result += d[i] * d[j]
    print(result)

if __name__ == '__main__':
    takoyaki_festival()