def main():
    n = int(input())
    k = 0
    while n >= 2**k:
        k += 1
    print(k-1)
main()
