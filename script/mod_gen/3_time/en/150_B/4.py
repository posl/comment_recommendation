def main():
    import sys
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().rstrip()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)

if __name__ == '__main__':
    main()