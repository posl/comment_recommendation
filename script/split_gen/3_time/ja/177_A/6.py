def main():
    #input
    D, T, S = map(int, input().split())
    #output
    if D/S <= T:
        print('Yes')
    else:
        print('No')
