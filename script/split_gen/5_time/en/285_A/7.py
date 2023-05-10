def main():
    a,b = map(int,input().split())
    if b-a==1 or a-b==1:
        print("Yes")
    else:
        print("No")
