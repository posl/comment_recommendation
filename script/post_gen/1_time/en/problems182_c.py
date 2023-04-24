Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    n = len(N)
    if n == 1:
        if int(N)%3 == 0:
            print(0)
        else:
            print(-1)
    elif n == 2:
        if int(N)%3 == 0:
            print(0)
        else:
            print(1)
    else:
        N = list(N)
        N = [int(i) for i in N]
        sum_N = sum(N)
        if sum_N%3 == 0:
            print(0)
        else:
            if sum_N%3 == 1:
                if 1 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 4 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 7 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                else:
                    if n <= 5:
                        print(2)
                    else:
                        print(1)
            else:
                if 2 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 5 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 8 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                else:
                    if n <= 5:
                        print(2)
                    else:
                        print(1)

=======
Suggestion 2

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sum(N)
    if N % 3 == 0:
        print(0)
    elif len(N) == 1:
        print(-1)
    else:
        if N % 3 == 1:
            if 1 in N or 4 in N or 7 in N:
                print(1)
            elif 2 in N or 5 in N or 8 in N:
                print(2)
            else:
                print(-1)
        elif N % 3 == 2:
            if 2 in N or 5 in N or 8 in N:
                print(1)
            elif 1 in N or 4 in N or 7 in N:
                print(2)
            else:
                print(-1)

=======
Suggestion 3

def main():
    N = input()
    if N == '0':
        print(0)
        return
    if N == '1':
        print(-1)
        return
    if N == '2':
        print(-1)
        return
    if N == '3':
        print(0)
        return
    if N == '4':
        print(-1)
        return
    if N == '5':
        print(1)
        return
    if N == '6':
        print(0)
        return
    if N == '7':
        print(-1)
        return
    if N == '8':
        print(1)
        return
    if N == '9':
        print(0)
        return
    if N == '10':
        print(1)
        return
    if N == '11':
        print(0)
        return
    if N == '12':
        print(0)
        return
    if N == '13':
        print(1)
        return
    if N == '14':
        print(2)
        return
    if N == '15':
        print(0)
        return
    if N == '16':
        print(1)
        return
    if N == '17':
        print(0)
        return
    if N == '18':
        print(0)
        return
    if N == '19':
        print(1)
        return
    if N == '20':
        print(2)
        return
    if N == '21':
        print(1)
        return
    if N == '22':
        print(0)
        return
    if N == '23':
        print(1)
        return
    if N == '24':
        print(2)
        return
    if N == '25':
        print(3)
        return
    if N == '26':
        print(2)
        return
    if N == '27':
        print(1)
        return
    if N == '28':
        print(0)
        return
    if N == '29':
        print(1)
        return
    if N == '30':
        print(0)
        return
    if N == '31':
        print(1)
        return
    if N == '32':
        print(2)

=======
Suggestion 4

def main():
    n = input()
    l = len(n)
    mod3 = [0, 0, 0]
    for i in range(l):
        mod3[int(n[i]) % 3] += 1
    if mod3[0] > 0:
        print(0)
    elif mod3[1] > 1:
        print(1)
    elif mod3[2] > 1:
        print(1)
    elif mod3[1] == 1 and mod3[2] == 1:
        if l > 1:
            print(2)
        else:
            print(-1)
    else:
        print(-1)

=======
Suggestion 5

def main():
    N = input()
    a = [int(i) for i in N]
    if sum(a) % 3 == 0:
        print(0)
        return

    if len(N) == 1:
        print(-1)
        return

    if len(N) == 2:
        if (a[0] + a[1]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return

    if len(N) == 3:
        if (a[0] + a[1] + a[2]) % 3 == 0:
            print(0)
        elif (a[0] + a[1]) % 3 == 0 or (a[1] + a[2]) % 3 == 0 or (a[0] + a[2]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return

    if len(N) == 4:
        if (a[0] + a[1] + a[2] + a[3]) % 3 == 0:
            print(0)
        elif (a[0] + a[1] + a[2]) % 3 == 0 or (a[1] + a[2] + a[3]) % 3 == 0 or (a[0] + a[1] + a[3]) % 3 == 0:
            print(1)
        elif (a[0] + a[1]) % 3 == 0 or (a[1] + a[2]) % 3 == 0 or (a[2] + a[3]) % 3 == 0 or (a[0] + a[2]) % 3 == 0 or (a[0] + a[3]) % 3 == 0 or (a[1] + a[3]) % 3 == 0:
            print(2)
        else:
            print(-1)
        return

    if len(N) == 5:
        if (a[0] + a[1] + a[2] + a[3] + a[4]) % 3 == 0:
            print(0)
        elif (a[0] + a

=======
Suggestion 6

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sorted(N, reverse=True)
    if sum(N) % 3 == 0:
        print(0)
    elif sum(N) % 3 == 1:
        if len(N) == 1:
            print(-1)
        elif len(N) == 2:
            if N[1] % 3 == 1:
                print(-1)
            else:
                print(1)
        else:
            if N[-1] % 3 == 1:
                print(1)
            elif N[-2] % 3 == 1:
                print(2)
            else:
                print(-1)
    else:
        if len(N) == 1:
            print(-1)
        elif len(N) == 2:
            if N[1] % 3 == 2:
                print(-1)
            else:
                print(1)
        else:
            if N[-1] % 3 == 2:
                print(1)
            elif N[-2] % 3 == 2:
                print(2)
            else:
                print(-1)

main()

I got a WA on this problem. I don't know why. Can someone help me with this?

Thanks

Last edited by a moderator: May 15, 2020

I don't know why.

=======
Suggestion 7

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sorted(N)
    N = [str(i) for i in N]
    N = ''.join(N)
    N = int(N)
    if N % 3 == 0:
        print(0)
    elif N % 3 == 1:
        if len(N) == 1:
            print(-1)
        else:
            for i in range(len(N)):
                if int(N[i]) % 3 == 1:
                    print(1)
                    break
                elif int(N[i]) % 3 == 2 and len(N) > 2:
                    print(2)
                    break
                elif int(N[i]) % 3 == 2 and len(N) == 2:
                    print(-1)
                    break
    else:
        if len(N) == 1:
            print(-1)
        else:
            for i in range(len(N)):
                if int(N[i]) % 3 == 2:
                    print(1)
                    break
                elif int(N[i]) % 3 == 1 and len(N) > 2:
                    print(2)
                    break
                elif int(N[i]) % 3 == 1 and len(N) == 2:
                    print(-1)
                    break

=======
Suggestion 8

def main():
    N = input()
    N = list(map(int, N))
    N = N[::-1]
    N = sum(N)
    if N % 3 == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 9

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]

    #print(N)

    #print(sum(N))

    if sum(N)%3 == 0:
        print(0)
        exit()

    if len(N) == 1:
        print(-1)
        exit()

    if len(N) == 2:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            print(-1)
            exit()

    if len(N) == 3:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            print(1)
            exit()

    if len(N) == 4:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            if N[0]%3 == 0 or N[1]%3 == 0 or N[2]%3 == 0 or N[3]%3 == 0:
                print(1)
                exit()
            else:
                print(-1)
                exit()

    if len(N) == 5:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            if N[0]%3 == 0 or N[1]%3 == 0 or N[2]%3 == 0 or N[3]%3 == 0 or N[4]%3 == 0:
                print(1)
                exit()
            else:
                if (N[0] + N[1])%3 == 0 or (N[0] + N[2])%3 == 0 or (N[0] + N[3])%3 == 0 or (N[0] + N[4])%3 == 0 or (N[1] + N[2])%3 == 0 or (N[1] + N[3])%3 == 0 or (N[1] + N[4])%3 == 0 or (N[2] + N[3])%3 == 0 or (N[2] + N[4])%3 == 0 or (N[3] + N[4])%3 == 0:
                    print(2)
                    exit()
                else:
                    print(-1)

=======
Suggestion 10

def main():
    N = input()
    #print(N)
    #print(len(N))
    k = len(N)
    #print(k)
    #print(int(N[0]))
    #print(int(N[1]))
    #print(int(N[2]))
    #print(int(N[3]))
    #print(int(N[4]))
    #print(int(N[5]))
    #print(int(N[6]))
    #print(int(N[7]))
    #print(int(N[8]))
    #print(int(N[9]))
    #print(int(N[10]))
    #print(int(N[11]))
    #print(int(N[12]))
    #print(int(N[13]))
    #print(int(N[14]))
    #print(int(N[15]))
    #print(int(N[16]))
    #print(int(N[17]))
    #print(int(N[18]))
    #print(int(N[19]))
    #print(int(N[20]))
    #print(int(N[21]))
    #print(int(N[22]))
    #print(int(N[23]))
    #print(int(N[24]))
    #print(int(N[25]))
    #print(int(N[26]))
    #print(int(N[27]))
    #print(int(N[28]))
    #print(int(N[29]))
    #print(int(N[30]))
    #print(int(N[31]))
    #print(int(N[32]))
    #print(int(N[33]))
    #print(int(N[34]))
    #print(int(N[35]))
    #print(int(N[36]))
    #print(int(N[37]))
    #print(int(N[38]))
    #print(int(N[39]))
    #print(int(N[40]))
    #print(int(N[41]))
    #print(int(N[42]))
    #print(int(N[43]))
    #print(int(N[44]))
    #print(int(N[45]))
    #print(int(N[46]))
    #print(int(N[47]))
    #print(int(N[48]))
    #print(int(N[49]))
    #print(int(N[50]))
    #print(int(N[51]))
    #print(int(N[52]))
    #print(int(N[53]))
    #print(int(N[54]))
    #print(int(N[55]))
    #print(int(N[56]))
    #print(int(N[57]))
    #print(int(N[58
