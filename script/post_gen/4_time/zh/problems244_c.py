Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(1,2*n+2):
        a.append(i)
    judge = 0
    while(1):
        if judge == 0:
            print(a.pop(0))
            judge = 1
        elif judge == 1:
            b = int(input())
            if b == 0:
                break
            else:
                a.remove(b)
                judge = 0

=======
Suggestion 2

def get_input():
    return int(input())

=======
Suggestion 3

def main():
    n = int(input())
    nums = [i for i in range(1, 2*n+2)]
    for i in range(1, 2*n+2):
        print(nums.pop(0))
        flush()
        a = int(input())
        if a == 0:
            break
        nums.remove(a)
        b = nums.pop(-1)
        print(b)
        flush()
        c = int(input())
        if c == 0:
            break
        nums.remove(c)
        nums.insert(0, a)
    exit()

=======
Suggestion 4

def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    left = 1
    right = 2*n+1
    while True:
        mid = (left+right)//2
        print(mid)
        judge = int(input())
        if judge == 0:
            break
        if judge == -1:
            right = mid
        else:
            left = mid
    return
solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(range(1,2*N+2))
    B = []
    while True:
        a = int(input())
        if a == 0:
            break
        A.remove(a)
        b = A.pop()
        B.append(b)
        print(b)
        A.remove(b)
main()

=======
Suggestion 6

def main():
    n = int(input())
    a = 0
    b = 2*n+1
    while True:
        print((a+b)//2)
        a = int(input())
        if a == 0:
            break
        if a < (a+b)//2:
            b = (a+b)//2
        else:
            a = (a+b)//2

=======
Suggestion 7

def main():
    #print("start")
    N = int(input())
    #print(N)
    if N == 1:
        print(1)
        #print("end")
        return
    list = [0]*(2*N+1)
    list[0] = -1
    list[1] = -1
    list[2] = -1
    list[3] = -1
    list[4] = -1
    list[5] = -1
    list[6] = -1
    list[7] = -1
    list[8] = -1
    list[9] = -1
    list[10] = -1
    list[11] = -1
    list[12] = -1
    list[13] = -1
    list[14] = -1
    list[15] = -1
    list[16] = -1
    list[17] = -1
    list[18] = -1
    list[19] = -1
    list[20] = -1
    list[21] = -1
    list[22] = -1
    list[23] = -1
    list[24] = -1
    list[25] = -1
    list[26] = -1
    list[27] = -1
    list[28] = -1
    list[29] = -1
    list[30] = -1
    list[31] = -1
    list[32] = -1
    list[33] = -1
    list[34] = -1
    list[35] = -1
    list[36] = -1
    list[37] = -1
    list[38] = -1
    list[39] = -1
    list[40] = -1
    list[41] = -1
    list[42] = -1
    list[43] = -1
    list[44] = -1
    list[45] = -1
    list[46] = -1
    list[47] = -1
    list[48] = -1
    list[49] = -1

=======
Suggestion 8

def main():
    n = int(input())
    print(1)
    flush()
    a = int(input())
    if a == 2:
        print(3)
        flush()
        a = int(input())
        if a == 4:
            print(5)
            flush()
            a = int(input())
            if a == 6:
                print(7)
                flush()
                a = int(input())
                if a == 8:
                    print(9)
                    flush()
                    a = int(input())
                    if a == 10:
                        print(11)
                        flush()
                        a = int(input())
                        if a == 12:
                            print(13)
                            flush()
                            a = int(input())
                            if a == 14:
                                print(15)
                                flush()
                                a = int(input())
                                if a == 16:
                                    print(17)
                                    flush()
                                    a = int(input())
                                    if a == 18:
                                        print(19)
                                        flush()
                                        a = int(input())
                                        if a == 20:
                                            print(21)
                                            flush()
                                            a = int(input())
                                            if a == 22:
                                                print(23)
                                                flush()
                                                a = int(input())
                                                if a == 24:
                                                    print(25)
                                                    flush()
                                                    a = int(input())
                                                    if a == 26:
                                                        print(27)
                                                        flush()
                                                        a = int(input())
                                                        if a == 28:
                                                            print(29)
                                                            flush()
                                                            a = int(input())
                                                            if a == 30:
                                                                print(31)
                                                                flush()
                                                                a = int(input())
                                                                if a == 32:
                                                                    print(33)
                                                                    flush()
                                                                    a = int(input())
                                                                    if a == 34:
                                                                        print(35)
                                                                        flush()
                                                                        a = int(input())
                                                                        if a == 36:
                                                                            print(37)
                                                                            flush()
                                                                            a = int(input())
                                                                            if a == 38:
                                                                                print(39)
                                                                                flush()
                                                                                a = int(input())
                                                                                if a == 40:
                                                                                    print(41)
                                                                                    flush()
                                                                                    a = int(input())
                                                                                    if a == 42:
                                                                                        print(43)
                                                                                        flush()
                                                                                        a = int(input())
                                                                                        if a == 44:
                                                                                            print(45)
                                                                                            flush()
                                                                                            a = int(input())
                                                                                            if a == 46:
                                                                                                print(47)
                                                                                                flush()

=======
Suggestion 9

def main():
    n = int(input())
    used = [False] * (2 * n + 2)
    for i in range(n):
        a = int(input())
        used[a] = True
        b = int(input())
        if b == 0:
            break
        used[b] = True
        for j in range(1, 2 * n + 2):
            if not used[j]:
                print(j)
                used[j] = True
                break
    return
