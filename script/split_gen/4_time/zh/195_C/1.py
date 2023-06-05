def main():
    n = int(input())
    cnt = 0
    for i in range(1, 15):
        if n < 10 ** i:
            cnt += (n - 10 ** (i - 1) + 1) * i
            break
        else:
            cnt += (10 ** i - 10 ** (i - 1)) * i
    print(cnt)
