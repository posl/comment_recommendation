def main():
    K = int(input())
    n = 1
    while K > 0:
        if n % sum([int(i) for i in str(n)]) == 0:
            print(n)
            K -= 1
        n += 1

if __name__ == '__main__':
    main()