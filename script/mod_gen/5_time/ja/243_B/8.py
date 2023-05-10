def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_b = 0
    for i in range(n):
        if a[i] == b[i]:
            a_b += 1
    a_b2 = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                a_b2 += 1
    print(a_b)
    print(a_b2-a_b)

if __name__ == '__main__':
    main()