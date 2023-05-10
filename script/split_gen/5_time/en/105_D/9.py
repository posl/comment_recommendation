def findPairs(arr, n, m):
    # Create an empty hashmap to store
    # ending value of prefixes.
    mp = {}
    # Initialize count of even
    # and odd sum pairs.
    evenSum = 0
    oddSum = 0
    # Traverse through all prefixes.
    for i in range(n):
        # Find ending index of prefix.
        rem = arr[i] % m
        # If rem == 0, then add 1 to evenSum
        if (rem == 0):
            evenSum += 1
        else:
            oddSum += 1
        # If this sum is seen before,
        # then update count of even
        # and odd sum pairs.
        if rem in mp.keys():
            evenSum += mp[rem]
        else:
            mp[rem] = 0
        mp[rem] += 1
    # Return count of even and odd
    # sum pairs.
    return (evenSum * (evenSum - 1) // 2 + oddSum * (oddSum - 1) // 2 + evenSum)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(findPairs(arr, n, m))
