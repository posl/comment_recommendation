def main():
    # Take input
    x, k = map(int, input().split())
    # Round off to the nearest 10^i
    for i in range(k):
        if x % 10 == 0:
            x //= 10
        else:
            x -= 1
    # Print the answer
    print(x)
