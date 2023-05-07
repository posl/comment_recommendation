def main():
    n,m = map(int, input().split())
    a = [0]*n
    for i in range(m):
        b = list(map(int, input().split()))
        for j in range(b[0]):
            a[b[j+1]-1] += 1
    for i in range(n):
        if a[i] == 0:
            print("No")
            break
    else:
        print("Yes")
