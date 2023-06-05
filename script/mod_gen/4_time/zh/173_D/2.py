def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.append(a[0])
    a.append(a[1])
    sum = 0
    for i in range(n):
        sum += abs(a[i+1] - a[i])
    print(sum)

if __name__ == '__main__':
    main()