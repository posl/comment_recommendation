def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    b = [0] * n
    for i in range(1, n):
        b[a[i-1]-1] += 1
    for i in b:
        print(i)

if __name__ == '__main__':
    main()