def main():
    # read input
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    # process
    # 1. find the order of p and q
    # 2. find the difference of order of p and q
    # 3. print the difference
    print(abs(order(p) - order(q)))
