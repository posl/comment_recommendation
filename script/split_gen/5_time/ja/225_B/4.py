def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        tmp1, tmp2 = map(int, input().split())
        a.append(tmp1)
        b.append(tmp2)
    a.sort()
    b.sort()
    if a[0] != 1:
        print("No")
        return
    for i in range(1, N):
        if a[i-1] != i or b[i-1] != i+1:
            print("No")
            return
    print("Yes")
