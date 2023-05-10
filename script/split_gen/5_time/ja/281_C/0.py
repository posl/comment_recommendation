def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    time = 0
    for i in range(n):
        if t < time + a[i]:
            print(i+1,t-time)
            break
        time += a[i]
    else:
        print(n,t-time)
