def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            for k in range(j, int(n ** 0.5) + 1):
                if i * j * k <= n:
                    if i == j and j == k:
                        ans += 1
                    elif i == j or j == k:
                        ans += 3
                    else:
                        ans += 6
    print(ans)
