def main():
    W = int(input())
    if W <= 2:
        print("2")
        print("1 2")
    elif W <= 300:
        print(W)
        for i in range(1, W + 1):
            print(i, end=' ')
    else:
        print("300")
        for i in range(1, 301):
            print(i, end=' ')
