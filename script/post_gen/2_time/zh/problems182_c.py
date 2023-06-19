Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n):
    #n = input()
    n = int(n)
    k = len(str(n))
    if k == 1:
        return -1
    if k == 2:
        if n % 3 == 0:
            return 0
        else:
            return -1
    if k == 3:
        if n % 3 == 0:
            return 0
        else:
            return -1
    if k >= 4:
        if n % 3 == 0:
            return 0
        else:
            if n % 3 == 1:
                return 1
            else:
                return 2

=======
Suggestion 2

def main():
    n = int(input())
    k = len(str(n))
    if k == 1:
        if n % 3 == 0:
            print(0)
        else:
            print(-1)
        exit()
    if k == 2:
        if n % 3 == 0:
            print(0)
        elif n % 3 == 1:
            if 1 in list(map(int, list(str(n)))):
                print(1)
            else:
                print(-1)
        else:
            if 2 in list(map(int, list(str(n)))):
                print(1)
            else:
                print(-1)
        exit()
    if k == 3:
        if n % 3 == 0:
            print(0)
        elif n % 3 == 1:
            if 1 in list(map(int, list(str(n)))):
                print(1)
            elif 2 in list(map(int, list(str(n)))):
                print(2)
            else:
                print(-1)
        else:
            if 2 in list(map(int, list(str(n)))):
                print(1)
            elif 1 in list(map(int, list(str(n)))):
                print(2)
            else:
                print(-1)
        exit()
    if n % 3 == 0:
        print(0)
    elif n % 3 == 1:
        if 1 in list(map(int, list(str(n)))):
            print(1)
        elif 2 in list(map(int, list(str(n)))):
            print(2)
        else:
            print(-1)
    else:
        if 2 in list(map(int, list(str(n)))):
            print(1)
        elif 1 in list(map(int, list(str(n)))):
            print(2)
        else:
            print(-1)

=======
Suggestion 3

def main():
    n = input()
    n = int(n)
    n_list = list(str(n))
    n_list.reverse()
    #print(n_list)
    n_len = len(n_list)
    k = 0
    for i in range(n_len):
        if n_list[i] == '0':
            k += 1
        else:
            break
    #print(k)
    if k == n_len:
        print(-1)
    else:
        #print(n_list[k:])
        #print(len(n_list[k:]))
        sum = 0
        for i in range(len(n_list[k:])):
            sum += int(n_list[k+i])
        #print(sum)
        if sum % 3 == 0:
            print(k)
        else:
            print(-1)

=======
Suggestion 4

def main():
    n = input()
    k = len(n)
    s = 0
    for i in range(k):
        s += int(n[i])
    if s%3 == 0:
        print(0)
    elif k == 1:
        print(-1)
    elif k == 2:
        print(-1)
    elif k == 3:
        print(-1)
    else:
        if s%3 == 1:
            if n.count('1') > 0:
                print(1)
            elif n.count('4') > 0:
                print(1)
            elif n.count('7') > 0:
                print(1)
            elif n.count('2') > 1:
                print(2)
            elif n.count('5') > 1:
                print(2)
            elif n.count('8') > 1:
                print(2)
            else:
                print(-1)
        else:
            if n.count('2') > 0:
                print(1)
            elif n.count('5') > 0:
                print(1)
            elif n.count('8') > 0:
                print(1)
            elif n.count('1') > 1:
                print(2)
            elif n.count('4') > 1:
                print(2)
            elif n.count('7') > 1:
                print(2)
            else:
                print(-1)

=======
Suggestion 5

def main():
    N = input()
    k = len(N)
    if k == 1:
        if int(N) % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        for i in range(1, k):
            if int(N[i]) % 3 == 0:
                print(1)
                break
            else:
                if (int(N[i-1]) + int(N[i])) % 3 == 0:
                    print(2)
                    break
        else:
            print(-1)

=======
Suggestion 6

def main():
    n = input()
    k = len(n)
    n = int(n)
    for i in range(k):
        if n % 3 == 0:
            print(i)
            return
        n //= 10
    print(-1)

=======
Suggestion 7

def main():
    N = int(input())
    K = len(str(N))
    if N % 3 == 0:
        print(0)
        return
    for i in range(K):
        for j in range(K):
            if i == j:
                continue
            if (N - int(str(N)[i]) - int(str(N)[j])) % 3 == 0:
                print(1)
                return
    for i in range(K):
        for j in range(K):
            for k in range(K):
                if i == j or j == k or k == i:
                    continue
                if (N - int(str(N)[i]) - int(str(N)[j]) - int(str(N)[k])) % 3 == 0:
                    print(2)
                    return
    print(-1)

=======
Suggestion 8

def main():
    N = input()
    N_len = len(N)
    N_int = int(N)
    N_int_list = [int(i) for i in N]
    N_int_list.sort(reverse=True)
    #print(N_int_list)
    sum_N = sum(N_int_list)
    #print(sum_N)
    if sum_N%3 == 0:
        print(0)
    else:
        if N_int%3 == 0:
            print(0)
        else:
            if N_int%3 == 1:
                if 1 in N_int_list:
                    print(1)
                elif 4 in N_int_list:
                    print(1)
                elif 7 in N_int_list:
                    print(1)
                else:
                    print(-1)
            else:
                if 2 in N_int_list:
                    print(1)
                elif 5 in N_int_list:
                    print(1)
                elif 8 in N_int_list:
                    print(1)
                else:
                    print(-1)

=======
Suggestion 9

def main():
    n = int(input())
    if n % 3 == 0:
        print(0)
        return

    digit_sum = 0
    for c in str(n):
        digit_sum += int(c)

    if digit_sum % 3 == 0:
        print(1)
        return

    if n >= 100 and n % 3 == 1:
        print(2)
        return

    if n >= 10 and n % 3 == 2:
        print(2)
        return

    print(-1)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    a = [0] * n
    for i in range(n):
        a[i] = int(s[i])

    ans = -1
    for i in range(n):
        if a[i] % 3 == 0:
            ans = 0
            break
        if a[i] % 3 == 1:
            if ans == -1:
                ans = 1
            elif ans == 2:
                ans = 1
            else:
                ans = 2
        if a[i] % 3 == 2:
            if ans == -1:
                ans = 2
            elif ans == 1:
                ans = 2
            else:
                ans = 1

    if ans == -1:
        print(-1)
    else:
        print(ans)
