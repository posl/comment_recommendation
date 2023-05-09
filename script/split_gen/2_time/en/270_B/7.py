def main():
    # Read input
    X, Y, Z = map(int, input().split())
    # Check if Takahashi can reach the goal
    if abs(X) < abs(Z):
        print(-1)
        return
    # Check if the wall is between the origin and the goal
    if abs(Z) < abs(Y) < abs(X):
        print(abs(X) - abs(Y))
    else:
        print(abs(X))
