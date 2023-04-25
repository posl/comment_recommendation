Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s, t = map(int, input().split())
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
    print(count)

=======
Suggestion 2

def main():
    S, T = map(int, input().split())
    count = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    s, t = map(int, input().split())
    ans = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    s, t = map(int, input().split())
    count = 0
    for i in range(s+1):
        for j in range(s+1):
            for k in range(s+1):
                if i+j+k <= s and i*j*k <= t:
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    S, T = map(int, input().split())
    count = 0
    for a in range(0, S+1):
        for b in range(0, S+1):
            for c in range(0, S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1
    print(count)

=======
Suggestion 6

def problem_statement():
    print("How many triples of non-negative integers (a, b, c) satisfy a+b+c ≦ S and a × b × c ≦ T?")
    print("Constraints")
    print("0 ≦ S ≦ 100")
    print("0 ≦ T ≦ 10000")
    print("S and T are integers.")
    print("Input")
    print("Input is given from Standard Input in the following format:")
    print("S T")
    print("Output")
    print("Print the number of triples of non-negative integers (a,b,c) satisfying the conditions.")
    print("Sample Input 1")
    print("1 0")
    print("Sample Output 1")
    print("4")
    print("The triples (a,b,c) satisfying the conditions are (0,0,0), (0,0,1), (0,1,0), and (1,0,0) ― there are four of them.")
    print("Sample Input 2")
    print("2 5")
    print("Sample Output 2")
    print("10")
    print("Sample Input 3")
    print("10 10")
    print("Sample Output 3")
    print("213")
    print("Sample Input 4")
    print("30 100")
    print("Sample Output 4")
    print("2471")

=======
Suggestion 7

def problem214_b():
    S, T = map(int, input().split())
    count = 0
    for a in range(0, S+1):
        for b in range(0, S+1):
            for c in range(0, S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    s,t = map(int, input().split())
    count = 0
    for a in range(0, 101):
        for b in range(0, 101):
            for c in range(0, 101):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
    print(count)
