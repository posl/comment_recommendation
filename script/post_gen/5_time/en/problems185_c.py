Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    l = int(input())
    print(int((l-1)*(l-2)*(l-3)*(l-4)*(l-5)*(l-6)/(6*5*4*3*2*1)))

=======
Suggestion 2

def main():
    L = int(input())
    
    print((L-1)*(L-2)*(L-3)*(L-4)*(L-5)*(L-6)*(L-7)*(L-8)*(L-9)*(L-10)*(L-11)//(11*10*9*8*7*6*5*4*3*2*1))

main()

=======
Suggestion 3

def solve():
    L = int(input())
    ans = 1
    for i in range(1, 12):
        ans *= (L - i)
        ans //= i + 1
    print(ans)

solve()

=======
Suggestion 4

def main():
    L = int(input())
    print(int(L * (L-1) * (L-2) * (L-3) * (L-4) * (L-5) / (6 * 5 * 4 * 3 * 2 * 1)))

=======
Suggestion 5

def main():
    l = int(input())
    print(int((l-1)*(l-2)*(l-3)*(l-4)*(l-5)*(l-6)/720))

=======
Suggestion 6

def main():
    L = int(input())
    print(int((L-1)*(L-2)*(L-3)*(L-4)*(L-5)*(L-6)/720))

=======
Suggestion 7

def main():
    L = int(input())
    print(int(L*(L-1)*(L-2)*(L-3)*(L-4)*(L-5)/720))

=======
Suggestion 8

def count_ways(L):
    # base cases
    if L < 12:
        return 0
    if L == 12:
        return 1

    # recursive case
    return count_ways(L-1) + count_ways(L-4) + count_ways(L-7) + count_ways(L-10) + count_ways(L-13) + count_ways(L-16)

=======
Suggestion 9

def main():
    l = int(input())
    print(combination(l-1, 11))
