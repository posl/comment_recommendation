def main():
    n = int(input())
    a = input().split()
    a = list(map(int,a))
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            if abs(a[i] - a[j]) > max:
                max = abs(a[i] - a[j])
    print(max)

if __name__ == '__main__':
    main()