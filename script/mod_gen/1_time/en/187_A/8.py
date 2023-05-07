def main():
    # input
    A, B = map(int, input().split())
    # compute
    S_A = A//100 + (A%100)//10 + A%10
    S_B = B//100 + (B%100)//10 + B%10
    # output
    print(max(S_A, S_B))

if __name__ == '__main__':
    main()