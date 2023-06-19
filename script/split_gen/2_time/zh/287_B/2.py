def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a.append(input())
    for i in range(m):
        b.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if a[i][3:6] == b[j]:
                count += 1
    print(count)
