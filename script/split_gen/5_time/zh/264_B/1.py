def main():
    R,C = map(int,input().split())
    if R%2==0 and C%2==0:
        print("白色")
    elif R%2==1 and C%2==1:
        print("白色")
    else:
        print("黑色")
