def main():
    N = int(input())
    if N < 54:
        print("AGC" + str(N).zfill(3))
    else:
        print("AGC" + str(N + 1).zfill(3))
main()

if __name__ == '__main__':
    main()