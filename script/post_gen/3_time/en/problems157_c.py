Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        elif S[0] == 1:
            print(C[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11, sep='

')
        elif M == 1:
            if S[0] == 1:
                print(10 + C[0])
            elif S[0] == 2:
                print(10 * C[0])
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(10 * C[0] + C[1])
            elif S[0] == 2 and S[1] == 1:
                print(10 * C[1] + C[0])
            else:
                print(-1)
        else:
            print(-1)
    else:
        if M == 0:
            print(100, 101, 102, 103, 104, 105, 106, 107, 108, 109, sep='

')
        elif M == 1:
            if S[0] == 1:
                print(100 + C[0])
            elif S[0] == 2:
                print(10 * C[0] + 0)
            elif S[0] == 3:
                print(1 * C[0] + 0)
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(100 + 10 * C[0] + C[1])
            elif S[0] == 1 and S[1] == 3:
                print(100 + 1 * C[0] + C[1])
            elif S[0] == 2 and S[1] == 1:
                print(10 * C[1] + 0 + C[0

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    for i in range(1000):
        if len(str(i)) != N:
            continue
        flag = True
        for j in range(M):
            if int(str(i)[S[j] - 1]) != C[j]:
                flag = False
                break
        if flag:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())

    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11, sep='

')
        elif M == 1:
            if S[0] == 1:
                print(10 + C[0])
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                if C[0] == C[1]:
                    print(10 * C[0] + C[1])
                else:
                    print(-1)
            else:
                print(-1)
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178,

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = []
    C = []
    for i in range(M):
        s, c = map(int, input().split())
        S.append(s)
        C.append(c)
    if N == 1:
        if M == 0:
            print(0)
        else:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11, sep='

')
        elif M == 1:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0], 10 + C[0], sep='

')
            elif S[0] == 2:
                if C[0] == 0:
                    print(10, 11, sep='

')
                else:
                    print(10 + C[0], 11 + C[0], sep='

')
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1:
                if S[1] == 2:
                    if C[0] == 0:
                        if C[1] == 0:
                            print(-1)
                        else:
                            print(10 + C[1], 11 + C[1], sep='

')
                    else:
                        print(10 * C[0] + C[1], 11 * C[0] + C[1], sep='

')
                else:
                    print(-1)
            elif S[0] == 2:
                if S[1] == 1:
                    if C[1] == 0:
                        if C[0] == 0:
                            print(-1)
                        else:
                            print(10 + C[0], 11 + C[0], sep='

')
                    else:
                        print(10 * C[1] + C[0], 11 * C[1] + C[0], sep='

')
                else:
                    print(-1)
            else:
                print(-1)
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(100, 101

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = []
    C = []
    for i in range(M):
        s, c = map(int, input().split())
        S.append(s)
        C.append(c)
    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 10 + 1, C[0] * 10 + 2)
            elif S[0] == 2:
                print(C[0] + 10, C[0] + 20)
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(C[0] * 10 + C[1], C[0] * 10 + C[1] + 10)
            elif S[0] == 2 and S[1] == 1:
                print(C[0] + C[1] * 10, C[0] + C[1] * 10 + 1)
            else:
                print(-1)
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(100, 101, 102)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 100 + 10, C[0] * 100 + 11, C[0] * 100 + 12)
            elif S[0] == 2:
                print(C[0] * 10 + 100, C[0] * 10 + 101, C[0] * 10 + 102)
            elif S[0] == 3:
                print(C[0] + 100, C[0] + 101, C[0] + 102)
            else:
                print(-1)
        elif M == 2

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = []
    C = []
    for i in range(M):
        s, c = map(int, input().split())
        S.append(s)
        C.append(c)
    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(C[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        elif M == 1:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*10)
            else:
                print(C[0]*10 + 1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*10 + C[1])
            else:
                print(-1)
        else:
            print(-1)
    else:
        if M == 0:
            print(100)
        elif M == 1:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*100)
            elif S[0] == 2:
                print(C[0]*10 + 10)
            else:
                print(C[0]*100 + 1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*100 + C[1]*10)
            elif S[0] == 1 and S[1] == 3:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*100 + C[1])
            elif S[0] == 2 and S[1] == 3:
                print(C[0]*10 + C[1] + 10)
            else:
                print(-1)
        elif M == 3:
            if S[0] == 1 and S[1] ==

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    if M == 0:
        if N == 1:
            print(0)
            return
        else:
            print(10**(N-1))
            return
    else:
        S = [0]*M
        C = [0]*M
        for i in range(M):
            S[i], C[i] = map(int, input().split())
        if N == 1:
            if M == 1:
                print(C[0])
                return
            else:
                print(-1)
                return
        else:
            if M == 1:
                if S[0] == 1:
                    if C[0] == 0:
                        print(-1)
                        return
                    else:
                        print(str(C[0]) + str(0)*(N-1))
                        return
                else:
                    print(str(1) + str(C[0]) + str(0)*(N-2))
                    return
            else:
                if S[0] == 1:
                    if C[0] == 0:
                        print(-1)
                        return
                    else:
                        for i in range(1, M):
                            if S[i] == 1:
                                print(-1)
                                return
                else:
                    print(str(1) + str(C[0]) + str(0)*(N-2))
                    return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):

=======
Suggestion 8

def main():
    #input
    N, M = map(int, input().split())
    SC = [list(map(int, input().split())) for _ in range(M)]

    #compute
    if N == 1:
        if M == 0:
            ans = 0
        else:
            ans = SC[0][1]
    else:
        if M == 0:
            ans = 10**(N-1)
        else:
            ans = -1
            for i in range(10**(N-1), 10**N):
                flag = True
                for j in range(M):
                    if int(str(i)[SC[j][0]-1]) != SC[j][1]:
                        flag = False
                        break
                if flag:
                    ans = i
                    break

    #output
    print(ans)

=======
Suggestion 9

def main():
    ans = -1
    N, M = map(int, input().split())
    #print(N, M)
    sc = [list(map(int, input().split())) for i in range(M)]
    #print(sc)
    for i in range(10**(N-1), 10**N):
        #print(i)
        for j in range(M):
            #print(i, sc[j][0], sc[j][1])
            if int(str(i)[sc[j][0]-1]) != sc[j][1]:
                break
        else:
            ans = i
            break
    print(ans)
    return

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    a = [input().split() for _ in range(M)]
    for i in range(10**N):
        #print(i)
        if len(str(i)) == N:
            for j in range(M):
                if str(i)[int(a[j][0])-1] != a[j][1]:
                    break
                if j == M-1:
                    print(i)
                    return
    print(-1)
    return
