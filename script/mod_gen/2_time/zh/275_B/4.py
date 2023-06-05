def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_index = 0
    for i in range(1, n):
        if h[i] > h[max_index]:
            max_index = i
    print(max_index + 1)

if __name__ == '__main__':
    main()