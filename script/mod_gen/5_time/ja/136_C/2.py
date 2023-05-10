def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            continue
        if h[i] - h[i-1] >= 2:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()