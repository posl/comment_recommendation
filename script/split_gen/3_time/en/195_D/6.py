def solve(N, M, Q, W, V, X, L, R):
    pass
N, M, Q = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
X = list(map(int, input().split()))
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
for ans in solve(N, M, Q, W, V, X, L, R):
    print(ans)
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line with two integers N and K, the number of houses and the number of people, respectively.
The second line of the input gives the value of N integers P_1, P_2, ..., P_N, the prices of the houses.
Output
For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is the minimum possible total price, and z is the maximum possible total price.
Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ N ≤ 100.
1 ≤ K ≤ N.
1 ≤ P_i ≤ 10000, for all i.
Test set 1
K = 1.
Test set 2
No additional constraints.
Sample
Input
Output
3
4 1
100 300 200 400
4 2
100 300 200 400
4 4
100 300 200 400
Case #1: 100 100
Case #2: 300 500
Case #3: 400 400
In Sample Case #1, there is only one person, so they have to buy the house with the lowest price, 100.
In Sample Case #2, the first person buys the house with the lowest price, 100, and the second person buys the house with the second lowest price, 200.
In Sample Case #3, each person buys the house with the lowest price, 100.
