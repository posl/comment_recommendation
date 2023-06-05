def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    #print(a,b)
    a.sort()
    b.sort()
    #print(a,b)
    if a[0] == 1 and b.count(a[0]) == N-1:
        print("Yes")
    else:
        print("No")
