def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    #compute
    #1.
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    print(count)
    
    #2.
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count += 1
    print(count)

if __name__ == '__main__':
    main()