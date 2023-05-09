def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    result = [i for i in a if i != x]
    for i in result:
        print(i, end=" ")

if __name__ == '__main__':
    main()