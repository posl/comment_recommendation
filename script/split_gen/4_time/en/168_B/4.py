def main():
    #input
    K = int(input())
    S = input()
    #output
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')
