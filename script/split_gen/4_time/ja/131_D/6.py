def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    ans = 0
    for i in range(n):
        ans += a[i]
        if ans > b[i]:
            print("No")
            exit()
    print("Yes")
