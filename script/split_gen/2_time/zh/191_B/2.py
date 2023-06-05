def main():
    v,t,s,d = map(int, input().split())
    if d < v*t or v*s < d:
        print("Yes")
    else:
        print("No")
