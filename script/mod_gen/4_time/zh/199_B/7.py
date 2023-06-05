def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    count = 0
    for i in range(1,1001):
        flag = True
        for j in range(n):
            if a[j] > i or b[j] < i:
                flag = False
                break
        if flag == True:
            count += 1
    print(count)

if __name__ == '__main__':
    main()