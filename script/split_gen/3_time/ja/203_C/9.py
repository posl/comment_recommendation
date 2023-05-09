def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    ab.append([10**100+1,0])
    now = 0
    for a,b in ab:
        if a-now>k:
            print(now+k)
            exit()
        else:
            k+=b
            now = a
