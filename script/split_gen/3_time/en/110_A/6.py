def main():
    # Read the input
    A,B,C = map(int, input().split())
    
    # Find the maximum possible allowance
    maxAllowance = max(A+B+C, A+B*C, (A+B)*C, A*B*C, A*B+C, A*B+C)
    
    # Print the maximum possible allowance
    print(maxAllowance)
