def main():
    n,m = map(int,input().split())
    num = [0 for i in range(n)]
    for i in range(m):
        s,c = map(int,input().split())
        if num[s-1] != 0 and num[s-1] != c:
            print(-1)
            return
        num[s-1] = c
    if n != 1 and num[0] == 0:
        print(-1)
        return
    elif n == 1 and num[0] == 0:
        print(0)
        return
    else:
        if num[0] == 0:
            num[0] = 1
        print(''.join(map(str,num)))
        return
