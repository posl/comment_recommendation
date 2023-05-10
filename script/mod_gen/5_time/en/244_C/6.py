def main():
    n = int(input())
    for i in range(1,2*n+2):
        print(i)
        flush()
        a = int(input())
        if a == 0:
            break

if __name__ == '__main__':
    main()