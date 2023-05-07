def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    #1 x _ q: assign x_q to every element of A.
    #2 i _ q x _ q: add x_q to A _ {i _ q}.
    #3 i _ q: print the value of A _ {i _ q}.
    # (1, 2, 3)
    # (x, i, x)
    # (x, x, x)
    query = [(int(q[0]), int(q[1]), int(q[2]) if len(q) == 3 else 0) for q in query]
    #print(query)

if __name__ == '__main__':
    main()