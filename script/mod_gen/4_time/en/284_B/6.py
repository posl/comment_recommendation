def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len([i for i in a if i%2==1]))

if __name__ == '__main__':
    main()