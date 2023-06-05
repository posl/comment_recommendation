def main():
    n = int(input())
    if n < 10:
        print("AGC00%d" % n)
    elif n < 100:
        print("AGC0%d" % n)
    else:
        print("AGC%d" % n)
