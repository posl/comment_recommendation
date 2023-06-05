def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [i for i in range(1, n+1) if a[i-1] == b[i-1]]
    d = [i for i in range(1, n+1) if a[i-1] in b and a[i-1] != b[i-1]]
    print(len(c))
    print(len(d))
