def main():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if u == s:
        a = a-1
    elif u == t:
        b = b-1
