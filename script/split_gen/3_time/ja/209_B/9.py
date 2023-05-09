def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    t = 0
    for i in range(n):
        if i % 2 == 1:
            t += 1
    if x >= sum(a) - t:
        print("Yes")
    else:
        print("No")
