Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n <= 54:
        print('AGC' + str(n).zfill(3))
    else:
        print('AGC' + str(n + 1).zfill(3))

=======
Suggestion 2

def main():
    N = int(input())
    if N < 42:
        print('AGC' + str(N).zfill(3))
    else:
        print('AGC' + str(N + 1).zfill(3))

=======
Suggestion 3

def main():
    N = int(input())
    if N <= 54:
        print("AGC{:03d}".format(N))
    else:
        print("AGC{:03d}".format(N+1))

=======
Suggestion 4

def main():
    n = int(input())
    if n < 43:
        print("AGC%03d" % n)
    else:
        print("AGC%03d" % (n + 1))

=======
Suggestion 5

def agc(n):
    if n < 42:
        return 'AGC' + str(n).zfill(3)
    else:
        return 'AGC' + str(n + 1).zfill(3)

=======
Suggestion 6

def main():
    n = int(input())
    if n >= 42:
        print(f"AGC{n+1}")
    else:
        print(f"AGC{n:03}")

=======
Suggestion 7

def main():
    n = int(input())
    if n<=54:
        print(f"AGC{str(n).zfill(3)}")
    elif n==55:
        print("AGC054")
    elif n==56:
        print("AGC053")
    elif n==57:
        print("AGC052")
    elif n==58:
        print("AGC051")
    elif n==59:
        print("AGC050")
    elif n==60:
        print("AGC049")
    elif n==61:
        print("AGC048")
    elif n==62:
        print("AGC047")
    elif n==63:
        print("AGC046")
    elif n==64:
        print("AGC045")
    elif n==65:
        print("AGC044")
    elif n==66:
        print("AGC043")
    elif n==67:
        print("AGC042")
    elif n==68:
        print("AGC041")
    elif n==69:
        print("AGC040")
    elif n==70:
        print("AGC039")
    elif n==71:
        print("AGC038")
    elif n==72:
        print("AGC037")
    elif n==73:
        print("AGC036")
    elif n==74:
        print("AGC035")
    elif n==75:
        print("AGC034")
    elif n==76:
        print("AGC033")
    elif n==77:
        print("AGC032")
    elif n==78:
        print("AGC031")
    elif n==79:
        print("AGC030")
    elif n==80:
        print("AGC029")
    elif n==81:
        print("AGC028")
    elif n==82:
        print("AGC027")
    elif n==83:
        print("AGC026")
    elif n==84:
        print("AGC025")
    elif n==85:
        print("AGC024")
    elif n==86:
        print("AGC023")
    elif n==87:
        print("AGC022")
    elif n==88:
        print("AGC021")
    elif n==89:
        print("AGC020")
    elif n==90:
        print("AGC019")
    elif

=======
Suggestion 8

def main():
    n = int(input())
    if n < 42:
        print(f'AGC0{n}')
    else:
        print(f'AGC{n+1}')

=======
Suggestion 9

def main():
    # read input
    N = int(input())
    # write output
    if N <= 54:
        print('AGC' + str(N).zfill(3))
    else:
        print('AGC' + str(N + 1).zfill(3))

main()
