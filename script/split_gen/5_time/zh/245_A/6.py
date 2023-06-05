def main():
    a,b,c,d = map(int,input().split())
    if a>c:
        print("高桥")
    elif a<c:
        print("青木")
    elif a==c:
        if b>d:
            print("高桥")
        elif b<d:
            print("青木")
        elif b==d:
            print("高桥")
