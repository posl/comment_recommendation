def main():
    a,n = map(int,input().split())
    count = 0
    while n > 0:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        count += 1
    print(count)
