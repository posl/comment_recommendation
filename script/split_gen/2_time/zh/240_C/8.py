def main():
    N,X = map(int,input().split())
    a = [0 for i in range(N)]
    b = [0 for i in range(N)]
    for i in range(N):
        a[i],b[i] = map(int,input().split())
    for i in range(N):
        if X == a[i] or X == b[i]:
            print("Yes")
            return
    print("No")
