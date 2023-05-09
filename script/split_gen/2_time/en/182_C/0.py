def main():
    N = input()
    if len(N) == 1:
        if int(N) % 3 == 0:
            print(0)
        else:
            print(-1)
    elif len(N) == 2:
        if (int(N[0]) + int(N[1])) % 3 == 0:
            print(0)
        elif int(N) % 3 == 0:
            print(1)
        else:
            print(-1)
    else:
        k = len(N)
        N = [int(n) for n in N]
        S = sum(N)
        if S % 3 == 0:
            print(0)
        else:
            if S % 3 == 1:
                if k == 3 and N[0] == 1 or N[1] == 1 or N[2] == 1:
                    print(1)
                elif N.count(1) >= 2 or N.count(2) >= 2:
                    print(2)
                elif N.count(1) == 1 and N.count(2) == 1:
                    print(2)
                elif N.count(1) == 0 and N.count(2) == 0:
                    print(-1)
                else:
                    print(1)
            else:
                if k == 3 and N[0] == 2 or N[1] == 2 or N[2] == 2:
                    print(1)
                elif N.count(1) >= 2 or N.count(2) >= 2:
                    print(2)
                elif N.count(1) == 1 and N.count(2) == 1:
                    print(2)
                elif N.count(1) == 0 and N.count(2) == 0:
                    print(-1)
                else:
                    print(1)
main()
I got a TLE for test case 15. I am not sure what I am doing wrong. Can someone please help me with this? Thanks in advance.
I am new to python and I am trying to solve this problem. I am getting a TLE for test case 15. Can someone please help me with this? Thanks in advance.
N = input()
    if len(N) == 1:
        if int(N) % 3 == 0:
            print(0)
