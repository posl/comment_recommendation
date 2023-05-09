def main():
    #input
    C_1, C_2, C_3 = input().split()
    #compute
    if C_1 == C_2 == C_3:
        result = "Won"
    else:
        result = "Lost"
    #output
    print(result)
