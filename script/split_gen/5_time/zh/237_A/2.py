def main():
    N = int(input())
    if (-2**31 <= N) and (N <= 2**31 - 1):
        print("是")
    else:
        print("否")
