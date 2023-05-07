def main():
    N = int(input())
    for i in range(1, N+1):
        if i*(i+1)//2 >= N:
            print(i)
            break

if __name__ == '__main__':
    main()