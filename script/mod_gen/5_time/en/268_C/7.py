def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    p.insert(0,0)
    p.append(0)
    count = 0
    for i in range(1,n+1):
        if p[i] == i-1:
            count += 1
            p[i] = i
            p[i+1] = i+1
    print(count)

if __name__ == '__main__':
    main()