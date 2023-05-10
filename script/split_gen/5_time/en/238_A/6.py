def main():
    import sys
    n = int(sys.stdin.readline())
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")
main()
