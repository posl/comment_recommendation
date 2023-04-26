Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = str(N)
    if len(S) == 1:
        if int(S) % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        Nsum = sum([int(i) for i in S])
        if Nsum % 3 == 0:
            print(0)
        else:
            if Nsum % 3 == 1:
                if S.count('1') > 0 or S.count('4') > 0 or S.count('7') > 0:
                    if len(S) == 2:
                        print(1)
                    else:
                        print(0)
                else:
                    if S.count('2') > 1 or S.count('5') > 1 or S.count('8') > 1:
                        print(2)
                    else:
                        print(-1)
            else:
                if S.count('2') > 0 or S.count('5') > 0 or S.count('8') > 0:
                    if len(S) == 2:
                        print(1)
                    else:
                        print(0)
                else:
                    if S.count('1') > 1 or S.count('4') > 1 or S.count('7') > 1:
                        print(2)
                    else:
                        print(-1)

=======
Suggestion 2

def main():
    N = input()
    if int(N) % 3 == 0:
        print(0)
        return
    if len(N) == 1:
        print(-1)
        return
    N = list(map(int, N))
    N.sort()
    N = N[::-1]
    if N[-1] % 2 == 0:
        print(1)
        return
    if sum(N) % 3 == 0:
        print(2)
        return
    print(-1)
    return

=======
Suggestion 3

def main():
    N = int(input())
    Nstr = str(N)
    Nlen = len(Nstr)
    Nsum = sum(map(int, Nstr))
    if Nsum % 3 == 0:
        print(0)
        return
    if Nsum % 3 == 1:
        if "1" in Nstr or "4" in Nstr or "7" in Nstr:
            if Nlen == 1:
                print(-1)
                return
            print(1)
            return
        if Nlen == 2:
            print(-1)
            return
        print(2)
        return
    if Nsum % 3 == 2:
        if "2" in Nstr or "5" in Nstr or "8" in Nstr:
            if Nlen == 1:
                print(-1)
                return
            print(1)
            return
        if Nlen == 2:
            print(-1)
            return
        print(2)
        return

=======
Suggestion 4

def main():
    N = input()
    N = list(N)
    N = list(map(int,N))
    k = len(N)
    if k == 1:
        if N[0] % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    elif k == 2:
        if (N[0] + N[1]) % 3 == 0:
            print(0)
        elif (N[0] * 10 + N[1]) % 3 == 0:
            print(0)
        elif (N[0] + N[1] * 10) % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    else:
        if sum(N) % 3 == 0:
            print(0)
            return
        elif sum(N) % 3 == 1:
            if N.count(1) >= 1:
                print(1)
                return
            elif N.count(4) >= 1:
                print(1)
                return
            elif N.count(7) >= 1:
                print(1)
                return
            elif N.count(2) >= 1 and N.count(5) >= 1:
                print(2)
                return
            elif N.count(2) >= 1 and N.count(8) >= 1:
                print(2)
                return
            elif N.count(5) >= 1 and N.count(8) >= 1:
                print(2)
                return
            elif N.count(2) >= 2:
                print(2)
                return
            elif N.count(5) >= 2:
                print(2)
                return
            elif N.count(8) >= 2:
                print(2)
                return
            elif N.count(3) >= 1 and N.count(6) >= 1:
                print(2)
                return
            elif N.count(3) >= 1 and N.count(9) >= 1:
                print(2)
                return
            elif N.count(6) >= 1 and N.count(9) >= 1:
                print(2)
                return
            elif N.count(3) >= 2:
                print(2)
                return
            elif N.count

=======
Suggestion 5

def main():
    N = input()
    N_list = list(N)
    N_list = [int(i) for i in N_list]
    N_list.sort(reverse=True)
    N_list = [str(i) for i in N_list]
    N = ''.join(N_list)
    N = int(N)
    if N % 3 == 0:
        print(0)
        return
    elif N % 3 == 1:
        if N_list.count('1') > 0:
            print(1)
            return
        elif N_list.count('4') > 0:
            print(1)
            return
        elif N_list.count('7') > 0:
            print(1)
            return
        elif N_list.count('2') > 1:
            print(2)
            return
        elif N_list.count('5') > 1:
            print(2)
            return
        elif N_list.count('8') > 1:
            print(2)
            return
        elif N_list.count('2') > 0 and N_list.count('5') > 0:
            print(2)
            return
        elif N_list.count('2') > 0 and N_list.count('8') > 0:
            print(2)
            return
        elif N_list.count('5') > 0 and N_list.count('8') > 0:
            print(2)
            return
        elif N_list.count('2') > 0 and N_list.count('5') > 0 and N_list.count('8') > 0:
            print(2)
            return
        elif N_list.count('3') > 0 and N_list.count('6') > 0:
            print(2)
            return
        elif N_list.count('3') > 0 and N_list.count('9') > 0:
            print(2)
            return
        elif N_list.count('6') > 0 and N_list.count('9') > 0:
            print(2)
            return
        elif N_list.count('3') > 0 and N_list.count('6') > 0 and N_list.count('9') > 0:
            print(2)
            return
        elif N_list.count('3') > 1:
            print(3)
            return
        elif N_list.count('6') >

=======
Suggestion 6

def main():
    N = input()
    N = list(N)
    N.sort()
    if N[0] == '0':
        for i in range(len(N)):
            if N[i] != '0':
                N[0], N[i] = N[i], N[0]
                break
    if N[0] == '0':
        print(-1)
    else:
        N = list(map(int, N))
        if sum(N) % 3 == 0:
            print(0)
        else:
            for i in range(len(N)):
                if N[i] % 3 == sum(N) % 3:
                    print(1)
                    break
            else:
                for i in range(len(N)):
                    for j in range(i+1, len(N)):
                        if (N[i] + N[j]) % 3 == sum(N) % 3:
                            print(2)
                            break
                    else:
                        continue
                    break
                else:
                    print(-1)

=======
Suggestion 7

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sorted(N, reverse=True)
    if N[-1] == 0:
        print(0)
        return
    if sum(N) % 3 != 0:
        print(-1)
        return
    N = [str(i) for i in N]
    N = ''.join(N)
    print(len(N)-N.count('0'))

=======
Suggestion 8

def main():
    N = int(input())
    # 3の倍数を作ることができるか
    # 3の倍数を作るのに必要な最少の消す桁数を求める
    N_str = str(N)
    N_len = len(N_str)
    N_sum = sum(map(int, N_str))
    if N_sum % 3 == 0:
        print(0)
    elif N_len == 1:
        print(-1)
    elif N_sum % 3 == 1:
        if N_len == 2:
            if N_str[0] == '1' or N_str[1] == '1':
                print(1)
            else:
                print(-1)
        else:
            if N_str.count('1') >= 1 or N_str.count('4') >= 1 or N_str.count('7') >= 1:
                print(1)
            elif N_str.count('2') >= 2 or N_str.count('5') >= 2 or N_str.count('8') >= 2:
                print(2)
            else:
                print(-1)
    else:
        if N_len == 2:
            if N_str[0] == '2' or N_str[1] == '2':
                print(1)
            else:
                print(-1)
        else:
            if N_str.count('2') >= 1 or N_str.count('5') >= 1 or N_str.count('8') >= 1:
                print(1)
            elif N_str.count('1') >= 2 or N_str.count('4') >= 2 or N_str.count('7') >= 2:
                print(2)
            else:
                print(-1)

=======
Suggestion 9

def main():
    N = input()
    keta = len(N)
    #print(keta)
    N = int(N)
    if N%3 == 0:
        print(0)
        return
    elif keta == 1:
        print(-1)
        return
    elif keta == 2:
        if N%10 == 0 or N%10 == 5:
            print(1)
            return
        else:
            print(-1)
            return
    else:
        #print(N%3)
        #print(N%10)
        #print(N%10)
        #print(N%100)
        #print(N%1000)
        #print(N%10000)
        #print(N%100000)
        #print(N%1000000)
        #print(N%10000000)
        #print(N%100000000)
        #print(N%1000000000)
        #print(N%10000000000)
        #print(N%100000000000)
        #print(N%1000000000000)
        #print(N%10000000000000)
        #print(N%100000000000000)
        #print(N%1000000000000000)
        #print(N%10000000000000000)
        #print(N%100000000000000000)
        #print(N%1000000000000000000)
        if N%3 == 1:
            if N%10 == 1 or N%100 == 1 or N%1000 == 1 or N%10000 == 1 or N%100000 == 1 or N%1000000 == 1 or N%10000000 == 1 or N%100000000 == 1 or N%1000000000 == 1 or N%10000000000 == 1 or N%100000000000 == 1 or N%1000000000000 == 1 or N%10000000000000 == 1 or N%100000000000000 == 1 or N%1000000000000000 == 1 or N%10000000000000000 == 1 or N%100000000000000000 == 1 or N%1000000000000000000 == 1:
                print(1)
                return
            else:
                if keta ==
