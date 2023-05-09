def main():
    n = int(input())
    v = list(map(int, input().split()))
    if n == 2:
        if v[0] == v[1]:
            print(1)
        else:
            print(0)
    else:
        count1 = 0
        count2 = 0
        for i in range(n):
            if i % 2 == 0:
                if v[i] != v[0]:
                    count1 += 1
                if v[i] != v[1]:
                    count2 += 1
            else:
                if v[i] != v[1]:
                    count1 += 1
                if v[i] != v[0]:
                    count2 += 1
        print(min(count1, count2))

if __name__ == '__main__':
    main()