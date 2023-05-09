def main():
    # Read input
    X, Y = map(int, input().split())
    
    # Process
    if X > Y:
        if X - Y > 2:
            print("No")
        else:
            print("Yes")
    else:
        if Y - X > 2:
            print("No")
        else:
            print("Yes")
