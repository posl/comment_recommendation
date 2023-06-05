def main():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if sum(a) >= h:
        print("Yes")
    else:
        print("No")
