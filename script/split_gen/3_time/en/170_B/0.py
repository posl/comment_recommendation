def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        for j in range(X+1):
            if i + j == X and 2*i + 4*j == Y:
                print("Yes")
                return
    print("No")
