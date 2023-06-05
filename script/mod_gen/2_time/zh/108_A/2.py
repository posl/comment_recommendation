def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        for j in range(i, n):
            b.append(sorted(a[i:j+1])[(j+1-i)//2])
    print(sorted(b)[len(b)//2])
main()
