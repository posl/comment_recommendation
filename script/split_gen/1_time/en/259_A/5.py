def main():
    n,m,x,t,d = map(int, input().split())
    for i in range(m):
        if i < x:
            t += d
        else:
            break
    print(t)
