def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    ans_n = 0
    for i in range(2, 1001):
        tmp = 0
        for j in range(n):
            if a[j] % i == 0:
                tmp += 1
        if tmp >= ans_n:
            ans_n = tmp
            ans = i
    print(ans)
