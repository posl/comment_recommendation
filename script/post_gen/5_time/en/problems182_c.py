Synthesizing 5/10 solutions

=======
Suggestion 1

def main():
    N = input()
    if len(N) == 1:
        if int(N) % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        N = [int(i) for i in N]
        N.sort()
        N = N[::-1]
        sumN = sum(N)
        if sumN % 3 == 0:
            print(0)
        else:
            if sumN % 3 == 1:
                if 1 in N:
                    N.remove(1)
                    if sum(N) % 3 == 0:
                        print(1)
                    else:
                        if 2 in N:
                            N.remove(2)
                            if sum(N) % 3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
                else:
                    if 2 in N:
                        N.remove(2)
                        if sum(N) % 3 == 0:
                            print(2)
                        else:
                            print(-1)
                    else:
                        print(-1)
            elif sumN % 3 == 2:
                if 2 in N:
                    N.remove(2)
                    if sum(N) % 3 == 0:
                        print(1)
                    else:
                        if 1 in N:
                            N.remove(1)
                            if sum(N) % 3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
                else:
                    if 1 in N:
                        N.remove(1)
                        if sum(N) % 3 == 0:
                            print(2)
                        else:
                            print(-1)
                    else:
                        print(-1)
            else:
                print(-1)

=======
Suggestion 2

def main():
    n = int(input())
    if n%3 == 0:
        print(0)
        return
    if n%3 == 1:
        if n%10 == 1:
            if n%100 == 11:
                print(2)
            else:
                print(1)
        elif n%10 == 4:
            if n%100 == 14:
                print(2)
            else:
                print(1)
        elif n%10 == 7:
            if n%100 == 17:
                print(2)
            else:
                print(1)
        else:
            print(-1)
    else:
        if n%10 == 2:
            if n%100 == 22:
                print(2)
            else:
                print(1)
        elif n%10 == 5:
            if n%100 == 25:
                print(2)
            else:
                print(1)
        elif n%10 == 8:
            if n%100 == 28:
                print(2)
            else:
                print(1)
        else:
            print(-1)

=======
Suggestion 3

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort()
    sumN = sum(N)
    if sumN%3 == 0:
        print(0)
    else:
        if sumN%3 == 1:
            if 1 in N:
                if len(N) == 1:
                    print(-1)
                else:
                    N.remove(1)
                    sumN = sum(N)
                    if sumN%3 == 0:
                        print(1)
                    else:
                        if 2 in N:
                            N.remove(2)
                            sumN = sum(N)
                            if sumN%3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
            else:
                if 2 in N:
                    if len(N) == 1:
                        print(-1)
                    else:
                        N.remove(2)
                        sumN = sum(N)
                        if sumN%3 == 0:
                            print(1)
                        else:
                            if 1 in N:
                                N.remove(1)
                                sumN = sum(N)
                                if sumN%3 == 0:
                                    print(2)
                                else:
                                    print(-1)
                            else:
                                print(-1)
                else:
                    print(-1)
        else:
            if 2 in N:
                if len(N) == 1:
                    print(-1)
                else:
                    N.remove(2)
                    sumN = sum(N)
                    if sumN%3 == 0:
                        print(1)
                    else:
                        if 1 in N:
                            N.remove(1)
                            sumN = sum(N)
                            if sumN%3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
            else:
                if 1 in N:
                    if len(N) == 1:
                        print(-1)
                    else:
                        N.remove(1)
                        sumN = sum(N)
                        if sumN%3 == 0:
                            print(1)
                        else:
                            if 2 in N:
                                N.remove(2)
                                sumN = sum(N)
                                if sumN%3 == 0:
                                    print(2)
                                else:
                                    print(-1)
                            else:

=======
Suggestion 4

def main():
    n = input()
    n = list(map(int, n))
    n.sort()
    n = n[::-1]
    total = sum(n)
    if total % 3 == 0:
        print(0)
    else:
        if total % 3 == 1:
            for i in range(len(n)):
                if n[i] % 3 == 1:
                    n.pop(i)
                    break
            if len(n) == 0:
                print(-1)
            else:
                print(1)
        else:
            for i in range(len(n)):
                if n[i] % 3 == 2:
                    n.pop(i)
                    break
            if len(n) == 0:
                print(-1)
            else:
                print(1)

=======
Suggestion 5

def solve():
    N = input()
    k = len(N)
    N = list(N)
    N.sort(reverse=True)
    N = ''.join(N)
    N = int(N)

    if N % 3 == 0:
        return 0
    elif N % 3 == 1:
        if k == 1:
            return -1
        elif k == 2:
            return -1
        elif k == 3:
            if N % 3 == 1:
                return 1
            elif N % 3 == 2:
                return 2
        else:
            for i in range(k):
                if int(N[i]) % 3 == 1:
                    return 1
                elif int(N[i]) % 3 == 2:
                    return 2
            return -1
    elif N % 3 == 2:
        if k == 1:
            return -1
        elif k == 2:
            return -1
        elif k == 3:
            if N % 3 == 1:
                return 2
            elif N % 3 == 2:
                return 1
        else:
            for i in range(k):
                if int(N[i]) % 3 == 1:
                    return 2
                elif int(N[i]) % 3 == 2:
                    return 1
            return -1

print(solve())
