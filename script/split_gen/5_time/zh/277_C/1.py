def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    print(min(b)-max(a)+1 if min(b)-max(a)+1>0 else 0)
