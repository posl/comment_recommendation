def main():
    n = int(input())
    s = list(input())
    q = int(input())
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            s[a-1],s[b-1] = s[b-1],s[a-1]
        else:
            if n == 1:
                s[0],s[1] = s[1],s[0]
            else:
                s[0],s[1] = s[1],s[0]
                s[2],s[3] = s[3],s[2]
    print(''.join(s))
