def main():
    a,b,c,d,e = map(int, input().split())
    if a==b==c and d==e:
        print("Yes")
    elif a==b==d and c==e:
        print("Yes")
    elif a==b==e and c==d:
        print("Yes")
    elif a==c==d and b==e:
        print("Yes")
    elif a==c==e and b==d:
        print("Yes")
    elif a==d==e and b==c:
        print("Yes")
    elif b==c==d and a==e:
        print("Yes")
    elif b==c==e and a==d:
        print("Yes")
    elif b==d==e and a==c:
        print("Yes")
    elif c==d==e and a==b:
        print("Yes")
    else:
        print("No")
