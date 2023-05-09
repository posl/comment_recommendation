def main():
    a,b,c,d,e = map(int, input().split())
    if a==b==c and d==e:
        print("Yes")
    elif a==b and c==d==e:
        print("Yes")
    else:
        print("No")
