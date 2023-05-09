def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()