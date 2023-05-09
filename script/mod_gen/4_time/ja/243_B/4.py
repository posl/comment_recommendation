def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_count = 0
    b_count = 0
    for i in range(n):
        if a[i] == b[i]:
            a_count += 1
            b_count += 1
        else:
            for j in range(n):
                if a[i] == b[j]:
                    b_count += 1
                    break
    print(a_count)
    print(b_count - a_count)

if __name__ == '__main__':
    main()