def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = 0
        for j in range(n):
            if a[j] % 2 == 1:
                cnt += 1
        print(cnt)
