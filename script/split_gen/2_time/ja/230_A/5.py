def main():
    N = int(input())
    if N < 42:
        print("AGC{:03}".format(N))
    else:
        print("AGC{:03}".format(N+1))
