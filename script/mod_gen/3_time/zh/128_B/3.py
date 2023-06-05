def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input().split())
    arr.sort(key=lambda x: (-int(x[1]), x[0]))
    for i in range(n):
        print(arr[i][0])

if __name__ == '__main__':
    main()