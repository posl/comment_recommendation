def main():
    n = int(input())
    cnt = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j < n:
                cnt += 1
            else:
                break
    print(cnt)
