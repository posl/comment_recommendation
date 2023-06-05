def main():
    R, C = input().split()
    R = int(R)
    C = int(C)
    if (R + C) % 2 == 0:
        print("黑色")
    else:
        print("白色")
