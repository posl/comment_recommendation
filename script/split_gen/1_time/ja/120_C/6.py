def main():
    #input
    S = input()
    N = len(S)
    #compute
    reds = S.count('0')
    blues = S.count('1')
    #output
    print(min(reds,blues)*2)
