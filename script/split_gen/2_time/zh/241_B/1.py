def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if a[-1] >= b[-1]:
        print("No")
        return
    for i in range(m):
        if a[-1] >= b[i]:
            print("No")
            return
    print("Yes")
