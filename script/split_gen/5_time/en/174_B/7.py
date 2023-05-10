def main():
    N,D = map(int,input().split())
    count = 0
    for _ in range(N):
        X,Y = map(int,input().split())
        if X**2 + Y**2 <= D**2:
            count += 1
    print(count)
