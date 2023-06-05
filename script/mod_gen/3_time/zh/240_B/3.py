def main():
    num = int(input())
    data = list(map(int,input().split()))
    print(len(set(data)))

if __name__ == '__main__':
    main()