def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    a.append(0)
    k = 0
    for i in range(n):
        if a[i] != a[i+1]:
            print(k)
            k = 0
        else:
            k += 1

if __name__ == '__main__':
    main()