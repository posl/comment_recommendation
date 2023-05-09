def main():
    import sys
    #input
    x = list(map(int, sys.stdin.readline().strip().split()))
    print(x.index(0)+1)
