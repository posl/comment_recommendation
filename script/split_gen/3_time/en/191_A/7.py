def main():
    # Read input
    v, t, s, d = map(int, input().split())
    # Print output
    if d < v * t or v * s < d:
        print('Yes')
    else:
        print('No')
