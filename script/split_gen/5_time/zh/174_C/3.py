def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        x = 7
        cnt = 1
        while x % k != 0:
            x = (x * 10 + 7) % k
            cnt += 1
        print(cnt)
