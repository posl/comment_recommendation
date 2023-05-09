def main():
    N = int(input())
    i = 1
    while N > 0:
        N -= i
        i += 1
    print(i-1)

if __name__ == '__main__':
    main()