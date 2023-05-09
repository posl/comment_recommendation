def main():
    # Write your code here
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    if H == 1 and W == 1:
        print(0)
    elif H == 1 or W == 1:
        print(1)
    else:
        print(2)
