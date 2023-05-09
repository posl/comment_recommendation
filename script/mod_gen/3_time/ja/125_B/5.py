def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(sum([V[i]-C[i] if V[i]-C[i]>0 else 0 for i in range(N)]))

if __name__ == '__main__':
    main()