def main():
    a,b,k = map(int, input().split())
    count = 0
    while 1:
        if a >= b:
            break
        a += a * (k - 1)
        count += 1
    print(count)
main()
