def main():
    N = int(input())
    for i in range(N+1):
        print(i+1)
        if int(input()) == 0:
            return
        print(2*N+2-i)
        if int(input()) == 0:
            return
    return

if __name__ == '__main__':
    main()