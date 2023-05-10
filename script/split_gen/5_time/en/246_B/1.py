def main():
    A, B = map(int, input().split())
    print("{0:.10f} {1:.10f}".format((A-1)/(A+B-1), (B-1)/(A+B-1)))
