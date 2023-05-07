def main():
    N = int(input())
    if N < 41:
        print("AGC%03d" % N)
    elif N < 54:
        print("AGC%03d" % (N + 1))
    else:
        print("AGC054")
