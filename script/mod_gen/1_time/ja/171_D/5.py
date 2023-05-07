def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    
    sum_A = sum(A)
    A_dict = {i: A.count(i) for i in set(A)}
    
    for bc in BC:
        b, c = bc[0], bc[1]
        if b in A_dict:
            sum_A += (c - b) * A_dict[b]
            if c in A_dict:
                A_dict[c] += A_dict[b]
            else:
                A_dict[c] = A_dict[b]
            A_dict[b] = 0
        print(sum_A)

if __name__ == '__main__':
    main()