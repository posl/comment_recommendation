def main():
    n = int(input())
    v = list(map(int,input().split()))
    v.sort()
    res = (v[0] + v[1])/2
    for i in range(2,n):
        res = (res + v[i])/2
    print(res)

if __name__ == '__main__':
    main()