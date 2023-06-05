def main():
    n = int(input())
    nums = list(map(int, input().split()))
    min_xor = 2**30
    for i in range(n):
        xor = nums[i]
        for j in range(i+1, n):
            xor = xor ^ nums[j]
            min_xor = min(min_xor, xor)
    print(min_xor)
