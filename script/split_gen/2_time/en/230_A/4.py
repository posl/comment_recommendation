def main():
    n = int(input())
    if n < 43:
        print("AGC{:03d}".format(n))
    else:
        print("AGC{:03d}".format(n + 1))
