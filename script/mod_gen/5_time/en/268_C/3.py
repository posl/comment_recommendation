def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(len(p)):
        if p[i] == i:
            count += 1
    if count == len(p):
        print(count)
    else:
        count = 0
        for i in range(len(p)):
            if p[i] == i:
                count += 1
            else:
                if p[p[i]] == i:
                    count += 1
        print(count)

if __name__ == '__main__':
    main()