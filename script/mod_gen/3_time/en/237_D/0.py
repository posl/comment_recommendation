def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.insert(len(A), i+1)
    print(*A)

if __name__ == '__main__':
    main()