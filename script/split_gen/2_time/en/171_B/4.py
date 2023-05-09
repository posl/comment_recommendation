def main():
    # Read a line
    line = input()
    # Split a line
    n, k = map(int, line.split())
    # Read another line
    line = input()
    # Split another line
    p = list(map(int, line.split()))
    # Sort a list
    p.sort()
    # Print the answer
    print(sum(p[:k]))
