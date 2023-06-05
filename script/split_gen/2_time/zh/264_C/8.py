def main():
    R,C = map(int,input().split())
    if R%2 == 0 and C%2 == 0:
        print("白色")
    elif R%2 == 0 and C%2 != 0:
        print("黑色")
    elif R%2 != 0 and C%2 == 0:
        print("黑色")
    elif R%2 != 0 and C%2 != 0:
        print("白色")
