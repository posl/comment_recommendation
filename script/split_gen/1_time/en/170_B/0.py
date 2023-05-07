def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        j = X - i
        if i*2 + j*4 == Y:
            print("Yes")
            return
    print("No")
