def main():
    a = list(map(int, input().split()))
    #print(a)
    k = 0
    for i in range(1, 4):
        k = a[k]
    print(k)

if __name__ == '__main__':
    main()