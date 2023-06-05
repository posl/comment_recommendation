def main():
    # input
    k = int(input())
    a, b = map(int, input().split())
    # check
    if b // k * k >= a:
        print("OK")
    else:
        print("NG")
