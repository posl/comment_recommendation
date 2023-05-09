def main():
    N = int(input())
    if N < 42:
        print("AGC{}".format(str(N).zfill(3)))
    else:
        print("AGC{}".format(str(N+1).zfill(3)))
