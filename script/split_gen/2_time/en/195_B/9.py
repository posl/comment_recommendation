def main():
    # Read the input
    a, b, w = map(int, input().split())
    w *= 1000
    # If the range is too large, report that fact
    if a * 1000 > w:
        print("UNSATISFIABLE")
        return
    # Find the minimum and maximum possible numbers of oranges chosen
    min_oranges = 1000
    max_oranges = 0
    for i in range(1000):
        if a * i <= w and w <= b * i:
            min_oranges = min(min_oranges, i)
            max_oranges = max(max_oranges, i)
    # Output the result
    if min_oranges == 1000:
        print("UNSATISFIABLE")
    else:
        print(min_oranges, max_oranges)
