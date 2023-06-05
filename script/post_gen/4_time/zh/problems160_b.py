Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    print((x//500)*1000 + ((x%500)//5)*5)

=======
Suggestion 2

def main():
    x = int(input())
    print(int((x//500)*1000 + ((x%500)//5)*5))

=======
Suggestion 3

def main():
    x = int(input())
    a = x // 500
    x -= a * 500
    b = x // 5
    print(a * 1000 + b * 5)

=======
Suggestion 4

def calc_happiness(X):
    # 500円硬貨
    n_500 = X // 500
    X -= n_500 * 500
    # 5円硬貨
    n_5 = X // 5
    return n_500 * 1000 + n_5 * 5

=======
Suggestion 5

def main():
    x = int(input())
    answer = 0
    answer += (x // 500) * 1000
    x %= 500
    answer += (x // 5) * 5
    print(answer)

=======
Suggestion 6

def main():
    x = int(input())
    ans = 0
    ans += 1000 * (x // 500)
    ans += 5 * ((x % 500) // 5)
    print(ans)

=======
Suggestion 7

def main():
    x = int(input())
    print(x//500*1000 + (x%500)//5*5)

=======
Suggestion 8

def main():
    x = int(input())
    y = x//500
    z = x%500//5
    print(y*1000+z*5)
