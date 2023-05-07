def main():
    s,t = input().split()
    a,b = input().split()
    u = input()
    if u == s:
        print(int(a)-1, b)
    else:
        print(a, int(b)-1)
