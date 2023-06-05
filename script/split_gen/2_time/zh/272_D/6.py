def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1, -1, -1):
            for j in range(i-1, -1, -1):
                if (a[i] + a[j]) % 2 == 0:
                    print(a[i] + a[j])
                    break
                if j == 0:
                    print(-1)
                    break
            if a[i] % 2 == 0:
                break
