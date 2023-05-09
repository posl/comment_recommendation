def main():
    W = int(input())
    if W <= 2:
        print(1)
        print(W)
    elif W <= 4:
        print(2)
        print(1, W-1)
    elif W <= 300:
        print(3)
        print(1, 2, 3)
    else:
        print(4)
        print(1, 2, 3, W-6)
