def main():
    a,b,c = map(int,input().split())
    if a+b == c+c or a+a == b+c or b+b == a+c:
        print("Yes")
    else:
        print("No")
