def main():
    R, C = map(int, input().split())
    if R % 2 == 1:
        if C % 2 == 1:
            print("黑色")
        else:
            print("白色")
    else:
        if C % 2 == 1:
            print("白色")
        else:
            print("黑色")
