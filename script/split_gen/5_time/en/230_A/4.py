def main():
    N = int(input())
    if N <= 9:
        print("AGC00" + str(N))
    elif N <= 99:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))
main()
