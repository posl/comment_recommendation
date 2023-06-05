def main():
    r,c = map(int,input().split())
    if r%2==0:
        if c%2==0:
            print("白色")
        else:
            print("黑色")
    else:
        if c%2==0:
            print("黑色")
        else:
            print("白色")
