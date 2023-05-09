def main():
    N = int(input())
    if N <= 54:
        print("AGC{:0=3}".format(N+1))
    else:
        print("AGC{:0=3}".format(N))
