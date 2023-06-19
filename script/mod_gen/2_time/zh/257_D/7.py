def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(arr)

if __name__ == '__main__':
    main()