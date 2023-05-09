def main():
    n,m = map(int,input().split())
    min = 0
    max = 0
    for i in range(m):
        a,b = map(int,input().split())
        if a < min or min == 0:
            min = a
        if a > max:
            max = a
        if b < min:
            min = b
        if b > max:
            max = b
    if min == 1 and max == n:
        print("Yes")
    else:
        print("No")
