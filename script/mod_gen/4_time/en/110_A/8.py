def max_allowance(A,B,C):
    # A,B,C are the values on the integer panels
    #return the maximum possible allowance
    return max(A+B+C, A*B*C, (A+B)*C, A*(B+C))

if __name__ == '__main__':
    max_allowance()