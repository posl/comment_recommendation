Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
        for j in range(i+1, N+i):
            if ans[i] > ans[j%N]:
                ans[j%N] = ans[i]
            else:
                ans[i] += S[j%N]
    for i in ans:
        print(i)

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        for j in range(i, i+N):
            if ans[j % N] > ans[(j+1) % N] + S[j % N]:
                ans[j % N] = ans[(j+1) % N] + S[j % N]
    for i in range(N):
        print(ans[i])

main()

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
        for j in range(i, i + n):
            if ans[j % n] > ans[(j + 1) % n] + s[(j + 1) % n]:
                ans[j % n] = ans[(j + 1) % n] + s[(j + 1) % n]
    for i in range(n):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for i in range(N):
        T[i] = [T[i], i]
    T.sort()
    ans = [0] * N
    for t, i in T:
        ans[i] = t + S[i]
        S[(i+1)%N] = min(S[(i+1)%N], S[i])
    print(*ans, sep='

')

=======
Suggestion 5

def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]
    #N = 200000
    #S = [random.randint(1, 10**9) for _ in range(N)]
    #T = [random.randint(1, 10**9) for _ in range(N)]
    #print(N)
    #print(' '.join([str(x) for x in S]))
    #print(' '.join([str(x) for x in T]))
    #print()

    # min time to receive a gem
    min_time = [0] * N
    # next gem to receive
    next_gem = [0] * N
    # gem to receive
    gems_to_receive = [0] * N
    # gems to receive
    gems_to_receive_count = 0
    # gem to give
    gems_to_give = [0] * N
    # gems to give
    gems_to_give_count = 0
    # gem to give
    gem_to_give = 0
    # gems to give
    gems_to_give_count = 0
    # time
    t = 0

    # initial state
    for i in range(N):
        min_time[i] = T[i]
        next_gem[i] = i
        gems_to_receive[i] = i
        gems_to_receive_count += 1

    # main loop
    while True:
        #print('t', t)
        #print('gems_to_receive_count', gems_to_receive_count)
        #print('gems_to_give_count', gems_to_give_count)
        #print('gems_to_receive', gems_to_receive)
        #print('gems_to_give', gems_to_give)
        #print()

        # receive gems
        if gems_to_receive_count > 0:
            #print('gems_to_receive_count > 0')
            #print()
            #print('gems_to_receive_count', gems_to_receive_count)
            #print('gems_to_receive', gems_to_receive)
            #print()
            #print('gems_to_give_count', gems_to_give_count)
            #print('gems_to_give', gems_to_give)
            #print()
            #print('next_gem', next_gem)
            #print

=======
Suggestion 6

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    #Snuke 1 2 3 4 5 6 7 8
    #Snuke 8 1 2 3 4 5 6 7
    #Snuke 7 8 1 2 3 4 5 6
    #Snuke 6 7 8 1 2 3 4 5
    #Snuke 5 6 7 8 1 2 3 4
    #Snuke 4 5 6 7 8 1 2 3
    #Snuke 3 4 5 6 7 8 1 2
    #Snuke 2 3 4 5 6 7 8 1

    #Takahashi 1 2 3 4 5 6 7 8
    #Takahashi 8 1 2 3 4 5 6 7
    #Takahashi 7 8 1 2 3 4 5 6
    #Takahashi 6 7 8 1 2 3 4 5
    #Takahashi 5 6 7 8 1 2 3 4
    #Takahashi 4 5 6 7 8 1 2 3
    #Takahashi 3 4 5 6 7 8 1 2
    #Takahashi 2 3 4 5 6 7 8 1

    #Snuke 1 2 3 4 5 6 7 8
    #Snuke 8 1 2 3 4 5 6 7
    #Snuke 7 8 1 2 3 4 5 6
    #Snuke 6 7 8 1 2 3 4 5
    #Snuke 5 6 7 8 1 2 3 4
    #Snuke 4

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    #print(N)
    #print(S)
    #print(T)
    #print(type(S[0]))
    #print(type(T[0]))
    #print(S[0] + T[0])
    #print(S[0] + S[1] + T[0])
    #print(S[0] + S[1] + S[2] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + S[5] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + S[5] + S[6] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + S[5] + S[6] + S[7] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + S[5] + S[6] + S[7] + S[0] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + S[5] + S[6] + S[7] + S[0] + S[1] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + S[5] + S[6] + S[7] + S[0] + S[1] + S[2] + T[0])
    #print(S[0] + S[1] + S[2] + S[3] + S[4] + S[5]

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    tsum = sum(t)
    for i in range(n):
        if i == 0:
            print(tsum)
        elif i == 1:
            print(tsum)
        else:
            print(tsum - min(s[:i]))

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    #Snuke's next transaction time
    next_time = [0]*N
    #Snuke's next transaction type
    next_type = [0]*N
    #Snuke's next transaction target
    next_target = [0]*N
    #Snuke's next transaction time is Takahashi's
    for i in range(N):
        next_time[i] = T[i]
        next_type[i] = 0
        next_target[i] = i
    #Snuke's next transaction time is Snuke's
    for i in range(N):
        j = next_target[i]
        if next_time[j] > next_time[i] + S[i]:
            next_time[j] = next_time[i] + S[i]
            next_type[j] = 1
            next_target[j] = (i+1)%N
    #print(next_time)
    #print(next_type)
    #print(next_target)
    for i in range(N):
        print(next_time[i])
