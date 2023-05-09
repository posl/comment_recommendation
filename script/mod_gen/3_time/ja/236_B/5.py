def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a.count(i+1) == 1:
            print(i+1)
            break

if __name__ == '__main__':
    main()