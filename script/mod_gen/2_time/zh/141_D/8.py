def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    a.append(0)
    count = 0
    for i in range(n):
        if a[i] > a[i+1]:
            count += 1
        else:
            count += 1
            break
    print(count)
    return 0

if __name__ == '__main__':
    main()