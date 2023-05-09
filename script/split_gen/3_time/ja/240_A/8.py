def main():
    a,b = map(int,input().split())
    if a <= b:
        if a <= 4 and b >= 5:
            print("Yes")
        else:
            print("No")
    else:
        if b <= 4 and a >= 5:
            print("Yes")
        else:
            print("No")
