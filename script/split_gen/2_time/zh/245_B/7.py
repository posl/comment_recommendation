def main():
    a,b,c,d = map(int, input().split())
    if a > c:
        print("高桥")
    elif a == c and b > d:
        print("高桥")
    else:
        print("青木")
