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
