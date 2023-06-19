def main():
    n,k = map(int,input().split())
    snuke = [0 for i in range(n)]
    for i in range(k):
        d = int(input())
        a = list(map(int,input().split()))
        for j in range(d):
            snuke[a[j]-1] += 1
    count = 0
    for i in range(n):
        if snuke[i] == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()