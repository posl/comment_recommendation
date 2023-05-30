def main():
    import sys
    n = int(sys.stdin.readline().strip())
    print((n-1).bit_length())
main()
