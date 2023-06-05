def main():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    if h <= sum(a):
        print("Yes")
    else:
        print("No")
