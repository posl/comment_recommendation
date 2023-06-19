def solution():
    n = int(input())
    s = list(map(int,input().split()))
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1,n):
        a[i] = s[i] - s[i-1]
    print(" ".join(map(str,a)))

if __name__ == '__main__':
    solution()