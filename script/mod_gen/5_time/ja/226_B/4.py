def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append([int(i) for i in input().split()])
    l.sort(key=lambda x: x[1:])
    count = 1
    for i in range(n-1):
        if l[i] != l[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()