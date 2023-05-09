def main():
    # read input
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # remove elements equal to x
    a = [e for e in a if e != x]
    # print the remaining elements
    print(' '.join(map(str, a)))
