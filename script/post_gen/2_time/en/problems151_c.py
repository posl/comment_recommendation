Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AC = [0] * (N + 1)
    WA = [0] * (N + 1)
    for i in range(M):
        p, S = input().split()
        p = int(p)
        if S == "AC":
            AC[p] = 1
        else:
            if AC[p] == 0:
                WA[p] += 1
    AC = sum(AC)
    WA = sum([WA[i] if AC[i] else 0 for i in range(1, N + 1)])
    print(AC, WA)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    p = []
    S = []
    for i in range(M):
        p_i, S_i = input().split()
        p.append(int(p_i))
        S.append(S_i)
    #print(N, M)
    #print(p)
    #print(S)

    #print("1")
    #print("2")
    #print("3")
    #print("4")
    #print("5")
    #print("6")
    #print("7")
    #print("8")
    #print("9")
    #print("10")
    #print("11")
    #print("12")
    #print("13")
    #print("14")
    #print("15")
    #print("16")
    #print("17")
    #print("18")
    #print("19")
    #print("20")
    #print("21")
    #print("22")
    #print("23")
    #print("24")
    #print("25")
    #print("26")
    #print("27")
    #print("28")
    #print("29")
    #print("30")
    #print("31")
    #print("32")
    #print("33")
    #print("34")
    #print("35")
    #print("36")
    #print("37")
    #print("38")
    #print("39")
    #print("40")
    #print("41")
    #print("42")
    #print("43")
    #print("44")
    #print("45")
    #print("46")
    #print("47")
    #print("48")
    #print("49")
    #print("50")
    #print("51")
    #print("52")
    #print("53")
    #print("54")
    #print("55")
    #print("56")
    #print("57")
    #print("58")
    #print("59")
    #print("60")
    #print("61")
    #print("62")
    #print("63")
    #print("64")
    #print("65")
    #print("66")
    #print("67")
    #print("68")
    #print("69")
    #print("70")
    #print("71")
    #print("

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    p = []
    S = []
    for i in range(M):
        p_i, S_i = input().split()
        p.append(int(p_i))
        S.append(S_i)
    correct = 0
    penalty = 0
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        if S[i] == "AC":
            if AC[p[i]-1] == 0:
                AC[p[i]-1] = 1
                correct += 1
                penalty += WA[p[i]-1]
        else:
            WA[p[i]-1] += 1
    print(correct, penalty)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    ac = [False]*n
    wa = [0]*n
    for _ in range(m):
        p, s = input().split()
        p = int(p)-1
        if s == 'AC':
            ac[p] = True
        else:
            if not ac[p]:
                wa[p] += 1
    ans = [0, 0]
    for i in range(n):
        if ac[i]:
            ans[0] += 1
            ans[1] += wa[i]
    print(*ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = [0] * N
    P = [0] * N
    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            S[p - 1] = 1
        else:
            if S[p - 1] == 0:
                P[p - 1] += 1
    ans1 = 0
    ans2 = 0
    for i in range(N):
        if S[i] == 1:
            ans1 += 1
            ans2 += P[i]
    print(ans1, ans2)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0, 0)
        return
    ac = [0] * (N + 1)
    wa = [0] * (N + 1)
    for _ in range(M):
        p, S = input().split()
        p = int(p)
        if ac[p] == 0:
            if S == 'AC':
                ac[p] = 1
            else:
                wa[p] += 1
    AC = 0
    WA = 0
    for i in range(1, N + 1):
        if ac[i] == 1:
            AC += 1
            WA += wa[i]
    print(AC, WA)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    correct = [False] * N
    wa = [0] * N
    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1
        if s == "AC":
            correct[p] = True
        elif not correct[p]:
            wa[p] += 1
    print(sum(correct), sum(wa[i] for i in range(N) if correct[i]))
main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    p = [0 for _ in range(N + 1)]
    s = [0 for _ in range(N + 1)]
    for _ in range(M):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            if si == 'AC':
                s[pi] = 1
            else:
                p[pi] += 1
    ac = sum(s)
    wa = 0
    for i in range(1, N + 1):
        if s[i] == 1:
            wa += p[i]
    print('{} {}'.format(ac, wa))

=======
Suggestion 9

def main():
    input = sys.stdin.readline
    #N, M = map(int, input().split())
    #A = list(map(int, input().split()))
    #B = list(map(int, input().split()))
    #C = [list(map(int, input().split())) for _ in range(N)]
    N, M = map(int, input().split())
    AC = [0] * N
    WA = [0] * N
    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1
        if AC[p]:
            continue
        if s == 'AC':
            AC[p] = 1
        else:
            WA[p] += 1
    ans1 = sum(AC)
    ans2 = sum(WA[i] for i in range(N) if AC[i])
    print(ans1, ans2)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    correct = 0
    penalty = 0
    p = [0] * (N + 1)
    for i in range(M):
        pi, si = input().split()
        pi = int(pi)
        if si == "AC":
            if p[pi] == 0:
                correct += 1
                p[pi] = 1
        else:
            if p[pi] == 0:
                penalty += 1
    print(correct, penalty)
