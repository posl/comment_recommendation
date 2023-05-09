def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_set = set(a)
    b_set = set(b)
    
    cnt_1 = 0
    cnt_2 = 0
    
    for i in range(n):
        if a[i] == b[i]:
            cnt_1 += 1
    
    for i in range(n):
        if a[i] != b[i]:
            if a[i] in b_set:
                cnt_2 += 1
            if b[i] in a_set:
                cnt_2 += 1
    
    print(cnt_1)
    print(cnt_2//2)

if __name__ == '__main__':
    main()