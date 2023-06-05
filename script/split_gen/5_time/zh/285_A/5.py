def main():
    a,b = map(int,input().split())
    if b-a == 1 or b-a == 4:
        print("Yes")
    else:
        print("No")
