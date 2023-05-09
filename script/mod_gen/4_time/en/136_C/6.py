def main():
    n = int(input())
    h = list(map(int, input().split()))
    flag = True
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
        if h[i] > h[i + 1]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()