def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count = 0
    for i in range(1, 1001):
        flag = True
        for j in range(n):
            if i < a[j] or i > b[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()