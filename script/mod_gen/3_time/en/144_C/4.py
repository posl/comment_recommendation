def main():
    N = int(input())
    if N == 2:
        print(1)
        return
    for i in range(1, N):
        if i * i > N:
            print(i * 2 - 2)
            return
        if i * (i+1) > N:
            print(i * 2 - 1)
            return

if __name__ == '__main__':
    main()