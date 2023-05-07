def main():
    # Read input
    a, b, c, d, e, f = map(int, input().split())
    # Calculate the remainder
    ans = (a*b*c - d*e*f) % 998244353
    # Print the answer
    print(ans)
