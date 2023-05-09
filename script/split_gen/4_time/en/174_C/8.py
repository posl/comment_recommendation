def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    else:
        count = 1
        num = 7 % K
        while num != 0:
            num = (num * 10 + 7) % K
            count += 1
        print(count)
