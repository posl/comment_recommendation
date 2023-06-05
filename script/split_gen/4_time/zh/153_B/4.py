def main():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    if h <= sum(a):
        print("Yes")
    else:
        print("No")
