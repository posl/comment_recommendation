def main():
    n = int(input())
    l = [0]*n
    r = [0]*n
    for i in range(n):
        l[i],r[i] = map(int,input().split())
    l.sort()
    r.sort()
    print(l[0],r[-1]+1)
