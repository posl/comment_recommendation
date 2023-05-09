def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    happy = 0
    for i in range(n):
        if i == 0:
            if p[i] == n-1 or p[i] == 1:
                happy += 1
        elif i == n-1:
            if p[i] == n-2 or p[i] == 0:
                happy += 1
        else:
            if p[i] == i-1 or p[i] == i+1:
                happy += 1
    print(happy)

if __name__ == '__main__':
    main()