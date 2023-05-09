def main():
    K = int(input())
    #print(K)
    a = 2
    while True:
        b = K
        while b % a == 0:
            b = b // a
        if b == 1:
            print(a)
            break
        a += 1
main()

if __name__ == '__main__':
    main()