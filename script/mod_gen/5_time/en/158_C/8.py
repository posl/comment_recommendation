def main():
    #A, B = map(int, input().split())
    A, B = 2, 2
    for i in range(1, 1000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()