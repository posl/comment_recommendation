def main():
    a,n = map(int,input().split())
    count = 0
    while n != 1:
        if n % a == 0:
            n /= a
            count += 1
        else:
            n -= 1
            count += 1
        if n < 1:
            print(-1)
            return
    print(count)
