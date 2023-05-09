def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    print((v[0]+v[1])/2)
    for i in range(2, n):
        print((v[0]+v[i])/2)
    return

if __name__ == '__main__':
    main()