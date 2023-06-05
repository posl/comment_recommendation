def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            arr[q[1] - 1] = q[2]
        else:
            print(arr[q[1] - 1])

if __name__ == '__main__':
    main()