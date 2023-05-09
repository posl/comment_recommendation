def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    else:
        count = 1
        num = 7 % k
        while num != 0:
            num = (num * 10 + 7) % k
            count += 1
        print(count)
        return
