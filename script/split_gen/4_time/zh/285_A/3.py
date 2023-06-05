def main():
    a,b = map(int,input().split())
    if a in [1,3,5,7,9,11,13]:
        if b == a + 1:
            print("Yes")
        else:
            print("No")
    elif a in [2,4,6,8,10,12,14]:
        if b == a + 1 or b == a + 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
