def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    print("Yes" if t[0] in s and t[-1] in s and s.index(t[0]) < s.index(t[-1]) else "No")
