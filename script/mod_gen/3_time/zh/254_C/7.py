def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, k)
    #print(a)
    for i in range(n-k):
        if a[i] > a[i+k]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()