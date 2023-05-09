def main():
    W = int(input())
    if W<=6:
        print(3)
        print(1,2,3)
    else:
        print(W//2)
        print(*([2]*(W//2-1)+[3]))
