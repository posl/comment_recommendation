Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    print(min(N-1, happy + K*2))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    print(min(N-1, happy+2*K))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            happy += 1
    print(min(happy + 2 * K, N - 1))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(0, N-1):
        if S[i] == S[i+1]:
            happy += 1
    print(min(N-1, happy + 2 * K))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = input()
    happy = 0
    for i in range(n-1):
        happy += 1 if s[i] == s[i+1] else 0
    print(min(happy + 2*k, n-1))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = input()
    r = [0] * (n + 1)
    l = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'R':
            r[i + 1] = r[i] + 1
            l[i + 1] = 0
        else:
            l[i + 1] = l[i] + 1
            r[i + 1] = 0
    ans = 0
    for i in range(n + 1):
        ans = max(ans, min(r[i], k) + min(l[i], k))
    for i in range(n):
        if s[i] == s[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()

    #print(N, K, S)

    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1

    ans = min(N-1, happy + K*2)
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    s = input()
    start = s[0]
    count = 0
    for i in range(1, n):
        if s[i] == start:
            count += 1
    print(min(count + 2 * k, n - 1))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()

    # 連続するLとRの数を数える
    # 連続するLとRの数は、そのまま回転させたときの幸せな人の数になる
    # ただし、端については、端の方向に連続するLとRの数が幸せな人の数になる
    # また、端でない場所は、両隣の人の方向が同じなら幸せな人になる
    # 両隣の人の方向が違う場合は、端であるかどうかにかかわらず、幸せな人にならない
    # 両隣の人の方向が違う場合は、端であっても、回転させたときに幸せな人にならない
    # なので、端でない場所は、両隣の人の方向が同じなら幸せな人になる
    # 両隣の人の方向が違う場合は、幸せな人にならない
    # これを、端から順に数えていく
    # ただし、端でない場所は、両隣の人の方向が同じなら幸せな人になる
    # 両隣の人の方向が違う場合は、幸せな人にならない
    # これを、端から順に数えていく
    # ただし、端でない場所は、両隣の人の方向が同じなら幸せな人になる
    # 両隣の人の方向が違う場合は、幸せな人にならない
    # これを、端から順に数えていく

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()

    # 1. 180度回転すると、L->R, R->Lになる
    # 2. 2回180度回転すると、元に戻る
    # 3. 180度回転したあと、そのまま180度回転させると、元に戻る
    # 4. 180度回転したあと、もう一度180度回転させると、元に戻る
    # 5. 180度回転したあと、さらにもう一度180度回転させると、元に戻る
    # 6. 180度回転したあと、さらにもう一度180度回転させると、元に戻る
    # つまり、2回の180度回転で元に戻る。
    # つまり、K回の180度回転で元に戻る。
    # つまり、K回の180度回転で、最初の状態に戻る。
    # つまり、K回の180度回転で、最初の状態と同じ状態になる。
    # つまり、K回の180度回転で、最初の状態と同じ状態の中で、最大のhappyな人数を求めればよい。
    # つまり、K回の180度回転で、最初の状態と同じ状態の中で、最大のhappyな人数を求めればよい。
    # つまり、K回の180度回転で、最初の状態と同じ状態の中で、最大のhappyな人数を求めればよい。
    # つま
