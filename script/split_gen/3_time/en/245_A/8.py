def main():
    # Read the input
    A, B, C, D = map(int, input().split())
    # Compute the time difference in minutes
    if A == C:
        diff = B - D
    elif A < C:
        diff = (60 - D) + (B + (C - A - 1) * 60)
    else:
        diff = (60 - B) + (D + (A - C - 1) * 60)
    # Print the output
    if diff < 0:
        print("Aoki")
    else:
        print("Takahashi")
main()
I got a WA on this problem. The reason is that I didn’t take into account the fact that 0:00 is one minute before 0:01. I had to add a special case to handle this.
