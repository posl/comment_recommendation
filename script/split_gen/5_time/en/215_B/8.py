def main():
    n = int(input())
    k = 0
    while 1:
        if 2**k <= n:
            k += 1
        else:
            break
    print(k-1)
main()
