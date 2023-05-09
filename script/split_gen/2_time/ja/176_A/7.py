def main():
    n,x,t = map(int,input().split())
    time = 0
    while n > 0:
        n -= x
        time += t
    print(time)
