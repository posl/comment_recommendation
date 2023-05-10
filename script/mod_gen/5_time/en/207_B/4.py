def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
        exit()
    else:
        for i in range(1, 10**5):
            if A <= (B * i) + (C * i * D):
                print(i)
                exit()

if __name__ == '__main__':
    main()