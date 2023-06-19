def main():
    K = int(input())
    # K = 30
    # K = 123456789011
    # K = 280
    N = 1
    while True:
        if N % K == 0:
            print(N)
            break
        N += 1
main()
