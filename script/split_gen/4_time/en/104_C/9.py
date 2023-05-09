def main():
    # Read a line
    line = input()
    # Split by space
    line = line.split()
    # Convert to int
    D = int(line[0])
    G = int(line[1])
    # Read a line
    line = input()
    # Split by space
    line = line.split()
    # Convert to int
    p = [int(line[i]) for i in range(D)]
    # Read a line
    line = input()
    # Split by space
    line = line.split()
    # Convert to int
    c = [int(line[i]) for i in range(D)]
    # Initialize minimum number of problems
    min_n = 1000
    # Try all combination of problems
    for i in range(2 ** D):
        # Initialize total score
        total_score = 0
        # Initialize number of problems
        n = 0
        # Initialize maximum score
        max_score = 0
        # Try all problems
        for j in range(D):
            # If the j-th problem is solved
            if ((i >> j) & 1) == 1:
                # Add the score to the total score
                total_score += (j + 1) * 100 * p[j] + c[j]
                # Add the number of problems to the total number of problems
                n += p[j]
                # Update the maximum score
                max_score = (j + 1) * 100
        # If the total score is less than the objective
        if total_score < G:
            # Try to solve the problem with the maximum score
            for k in range(p[max_score // 100 - 1]):
                # If the total score is greater than or equal to the objective
                if total_score >= G:
                    # Stop
                    break
                # Add the score to the total score
                total_score += max_score
                # Add the number of problems to the total number of problems
                n += 1
        # If the total score is greater than or equal to the objective
        if total_score >= G:
            # Update the minimum number of problems
            min_n = min(min_n, n)
    # Print the minimum number of problems
    print(min_n)
