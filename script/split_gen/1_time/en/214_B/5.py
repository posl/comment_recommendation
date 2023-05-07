def main():
    # Read the input
    S, T = map(int, input().split())
    # Calculate the answer
    ans = 0
    for a in range(S+1):
        for b in range(S+1-a):
            c = S-a-b
            if a*b*c <= T:
                ans += 1
    # Output the answer
    print(ans)
