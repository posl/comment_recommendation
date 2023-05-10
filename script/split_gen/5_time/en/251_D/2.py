def main():
    W = int(input())
    if W <= 3:
        print(1)
        print(W)
    elif W <= 5:
        print(2)
        print(2, W-2)
    else:
        print(3)
        print(2, 3, W-5)
