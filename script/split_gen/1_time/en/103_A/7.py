def main():
    # Get input here
    A = [int(x) for x in input().strip().split()]
    # Calculate result here
    A.sort()
    print(A[2]-A[0])
