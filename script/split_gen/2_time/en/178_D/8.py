def main():
    # Read the input
    S = int(input())
    # Create a list of the possible numbers
    nums = list(range(3,S+1))
    # Create a list to hold the number of ways to make the sum
    ways = [0] * (S+1)
    # There is only one way to make the sum 0
    ways[0] = 1
    # Loop through the numbers
    for num in nums:
        # Loop through the ways to make the sum
        for i in range(num,S+1):
            # Add the number of ways to make the sum minus the current number
            ways[i] += ways[i-num]
    # Print the number of ways to make the sum
    print(ways[S] % 1000000007)
