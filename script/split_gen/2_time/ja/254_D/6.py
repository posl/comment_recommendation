def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j > n:
                break
            if i * j == int(i * j ** 0.5) ** 2:
                cnt += 1
    print(cnt)
