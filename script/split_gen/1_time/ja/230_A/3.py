def main():
    n = int(input())
    if n < 42:
        print("AGC{0:03d}".format(n))
    else:
        print("AGC{0:03d}".format(n+1))
