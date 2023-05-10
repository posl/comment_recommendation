def main():
    N = int(input())
    S, T = input().split()
    new_str = ''
    for i in range(N):
        new_str += (S[i] + T[i])
    print(new_str)

if __name__ == '__main__':
    main()