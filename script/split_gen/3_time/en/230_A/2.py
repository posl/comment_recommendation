def main():
    N = int(input())
    if N <= 54:
        print("AGC{:03d}".format(N))
    else:
        print("AGC{:03d}".format(N+1))
