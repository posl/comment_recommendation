def main():
    n,m = map(int,input().split())
    if n < 2 or n > 400 or m < 1 or m > 10**6:
        print("Wrong Input")
        return
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                print(0,end=' ')
            else:
                print(1,end=' ')
        print()
