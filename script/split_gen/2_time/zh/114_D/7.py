def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    num = [0] * (n+1)
    for i in range(2, n+1):
        j = 2
        while j * j <= i:
            if i % j == 0:
                num[j] += 1
                if i // j != j:
                    num[i // j] += 1
            j += 1
    ans = 0
    for i in range(2, n+1):
        if num[i] >= 74:
            ans += 1
        for j in range(i+1, n+1):
            if num[i] >= 2 and num[j] >= 24:
                ans += 1
            if num[i] >= 24 and num[j] >= 2:
                ans += 1
            if num[i] >= 4 and num[j] >= 14:
                ans += 1
            if num[i] >= 14 and num[j] >= 4:
                ans += 1
            for k in range(j+1, n+1):
                if num[i] >= 2 and num[j] >= 4 and num[k] >= 4:
                    ans += 1
                if num[i] >= 4 and num[j] >= 2 and num[k] >= 4:
                    ans += 1
                if num[i] >= 4 and num[j] >= 4 and num[k] >= 2:
                    ans += 1
    print(ans)
