def main():
    N,D = map(int,input().split())
    count = 0
    for i in range(N):
        x,y = map(int,input().split())
        if (x**2+y**2)**0.5 <= D:
            count += 1
    print(count)
