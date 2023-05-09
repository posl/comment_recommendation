def main():
    # Get input here
    N = int(input())
    A = list(map(int, input().split()))
    # Compute desired result
    result = 'Yes' if sorted(A) == list(range(1, N+1)) else 'No'
    # Print result
    print(result)
