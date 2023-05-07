def main():
    # Read data
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    # Calculate the angle of each vertex
    # If the angle is greater than 180 degrees, the quadrilateral is not convex
    angleA = calculate_angle(A, B, C)
    angleB = calculate_angle(B, C, D)
    angleC = calculate_angle(C, D, A)
    angleD = calculate_angle(D, A, B)
    if angleA > 180 or angleB > 180 or angleC > 180 or angleD > 180:
        print("No")
    else:
        print("Yes")
