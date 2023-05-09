def main():
    # Read input
    R = int(input())
    
    # Solve problem
    if R < 1200:
        contest = "ABC"
    elif R < 2800:
        contest = "ARC"
    else:
        contest = "AGC"
    
    # Print result
    print(contest)
