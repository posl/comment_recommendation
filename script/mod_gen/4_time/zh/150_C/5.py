def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    def permutation_to_number(l):
        if len(l) == 1:
            return 0
        return l[-1] + permutation_to_number([x-1 for x in l[:-1] if x > l[-1]])
    print(abs(permutation_to_number(p) - permutation_to_number(q)))

if __name__ == '__main__':
    main()