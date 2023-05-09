def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    else:
        num = 7
        cnt = 1
        while num % K != 0:
            num = num * 10 + 7
            cnt += 1
        print(cnt)
