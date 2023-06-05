def main():
    a,b,c,d,e = map(int,input().split())
    if (a==b and b==c) or (a==b and b==d) or (a==b and b==e) or (a==c and c==d) or (a==c and c==e) or (a==d and d==e) or (b==c and c==d) or (b==c and c==e) or (b==d and d==e) or (c==d and d==e):
        print("Yes")
    else:
        print("No")
