def main():
    # input
    k = int(input())
    a, b = map(int, input().split())
    # compute
    # output
    if a % k == 0 or b % k == 0 or (a // k) != (b // k):
        print("OK")
    else:
        print("NG")
