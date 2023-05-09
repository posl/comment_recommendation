def main():
    # input
    C = list(input())
    # compute
    if C[0] == C[1] == C[2]:
        result = 'Won'
    else:
        result = 'Lost'
    # output
    print(result)
