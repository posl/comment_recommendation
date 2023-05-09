def main():
    N = int(input())
    print(sum(1 for i in range(1,N+1) if len(str(i))%2 == 1))

if __name__ == '__main__':
    main()