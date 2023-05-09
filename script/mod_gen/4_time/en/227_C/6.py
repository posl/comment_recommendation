def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        ans += N // a * (N // a + 1) // 2
    print(ans)
main()
The first part of the answer is the sum of the number of triples with A=1, A=2, A=3, ..., A=N. The number of triples with A=a is the number of triples with A=a and B=1, A=a and B=2, A=a and B=3, ..., A=a and B=N. The number of triples with A=a and B=b is the number of triples with A=a and B=b and C=1, A=a and B=b and C=2, A=a and B=b and C=3, ..., A=a and B=b and C=N. The number of triples with A=a and B=b and C=c is the number of triples with A=a and B=b and C=c and a≦b≦c and abc≦N. The number of triples with A=a and B=b and C=c and a≦b≦c and abc≦N is the number of triples with A=a and B=b a

if __name__ == '__main__':
    main()