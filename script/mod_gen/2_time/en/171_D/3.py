def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0]*q
    c = [0]*q
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    count = [0]*10**5
    for i in range(n):
        count[a[i]-1] += 1
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        sum += (c[i]-b[i])*count[b[i]-1]
        count[c[i]-1] += count[b[i]-1]
        count[b[i]-1] = 0
        print(sum)

if __name__ == '__main__':
    main()