def main():
    # Read input
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    # Check if the quadrilateral is convex
    if check_convex(A, B, C, D):
        print("Yes")
    else:
        print("No")
