def main():
    # Get input data
    a = [int(x) for x in input().split()]
    # Sort the list
    a.sort()
    # Check if the difference between the first and second element is the
    # same as the difference between the second and third element
    if a[1] - a[0] == a[2] - a[1]:
        print("Yes")
    else:
        print("No")
