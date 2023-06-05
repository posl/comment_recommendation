def main():
    n,q = map(int,input().strip().split())
    s = input()
    ac = [0]*(n+1)
    for i in range(n):
        if s[i:i+2] == "AC":
            ac[i+1] = ac[i] + 1
        else:
            ac[i+1] = ac[i]
    for i in range(q):
        l,r = map(int,input().strip().split())
        print(ac[r-1]-ac[l-1])
