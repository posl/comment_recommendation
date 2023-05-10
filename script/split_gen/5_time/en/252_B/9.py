def main():
    # Take input from stdin
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # Sort the list a
    a.sort(reverse=True)
    # Get the max value of b
    max_b = max(b)
    # Get the index of max value of b
    max_b_index = b.index(max_b)
    # Get the max value of a
    max_a = a[0]
    # Check if max value of b is less than max value of a
    if max_b < max_a:
        print("Yes")
    else:
        print("No")
