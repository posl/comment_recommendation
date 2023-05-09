def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    mod = 10**9 + 7
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += a_list[i] * a_list[j]
            sum %= mod
    print(sum)
