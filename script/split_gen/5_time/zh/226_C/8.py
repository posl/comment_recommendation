def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t1,k1,*a1 = map(int,input().split())
        t.append(t1)
        k.append(k1)
        a.append(a1)
    print(t)
    print(k)
    print(a)
    print("end")
