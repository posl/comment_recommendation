def main():
    # Read the input
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    # Solve the problem
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N - a, K - a) + 1):
            # Try to take out a jewels from the left end and b jewels from the right end
            # The jewels in the middle are left in the cylinder
            # The jewels in your hand are not included in the cylinder
            # You can choose the order of the jewels in your hand
            # The number of jewels in your hand is a + b
            # The values of the jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The values of the jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The total value is the sum of the values of the jewels in your hand and the jewels in the cylinder
            # The jewels in the cylinder are in the original order
            # You can choose the order of the jewels in your hand
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1, ..., V_a
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}, V_{N-b+1}, ..., V_N
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1
