def main():
    arr = list(map(int, input().split()))
    count = 0
    while True:
        count += 1
        if count > 100:
            break
        arr[0] = arr[arr[0]]
        if arr[0] == 0:
            break
    print(arr[0])

if __name__ == '__main__':
    main()