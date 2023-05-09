def main():
    N, L = map(int, input().split())
    sum = 0
    min = 100000000
    for i in range(N):
        sum += L + i
        if abs(L + i) < abs(min):
            min = L + i
    print(sum - min)
