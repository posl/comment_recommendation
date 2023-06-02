Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N < 10:
        print("AGC00", N, sep="")
    elif N < 100:
        print("AGC0", N, sep="")
    else:
        print("AGC", N, sep="")

=======
Suggestion 2

def main():
    n = int(input())
    if n >= 1 and n <= 9:
        print('AGC00'+str(n))
    elif n >= 10 and n <= 99:
        print('AGC0'+str(n))
    else:
        print('AGC'+str(n))

=======
Suggestion 3

def main():
    N = int(input())
    if N <= 9:
        print("AGC00" + str(N))
    elif N <= 99:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))

=======
Suggestion 4

def main():
    N = int(input())
    if N < 10:
        print("AGC00"+str(N))
    elif N < 100:
        print("AGC0"+str(N))
    else:
        print("AGC"+str(N))

=======
Suggestion 5

def main():
    N = int(input())
    if N < 10:
        print("AGC00" + str(N))
    elif N < 100:
        print("AGC0" + str(N))
    else:
        print("AGC" + str(N))

main()

=======
Suggestion 6

def main():
    N = int(input())
    if N <= 21:
        print('AGC0' + str(N))
    else:
        print('AGC' + str(N + 2))

=======
Suggestion 7

def main():
    N = int(input())
    if N >= 1 and N <= 9:
        print('AGC00' + str(N))
    elif N >= 10 and N <= 99:
        print('AGC0' + str(N))
    else:
        print('AGC' + str(N))

=======
Suggestion 8

def main():
    n = int(input())
    if n == 1:
        print("AGC001")
    elif n == 2:
        print("AGC002")
    elif n == 3:
        print("AGC003")
    elif n == 4:
        print("AGC004")
    elif n == 5:
        print("AGC005")
    elif n == 6:
        print("AGC006")
    elif n == 7:
        print("AGC007")
    elif n == 8:
        print("AGC008")
    elif n == 9:
        print("AGC009")
    elif n == 10:
        print("AGC010")
    elif n == 11:
        print("AGC011")
    elif n == 12:
        print("AGC012")
    elif n == 13:
        print("AGC013")
    elif n == 14:
        print("AGC014")
    elif n == 15:
        print("AGC015")
    elif n == 16:
        print("AGC016")
    elif n == 17:
        print("AGC017")
    elif n == 18:
        print("AGC018")
    elif n == 19:
        print("AGC019")
    elif n == 20:
        print("AGC020")
    elif n == 21:
        print("AGC021")
    elif n == 22:
        print("AGC022")
    elif n == 23:
        print("AGC023")
    elif n == 24:
        print("AGC024")
    elif n == 25:
        print("AGC025")
    elif n == 26:
        print("AGC026")
    elif n == 27:
        print("AGC027")
    elif n == 28:
        print("AGC028")
    elif n == 29:
        print("AGC029")
    elif n == 30:
        print("AGC030")
    elif n == 31:
        print("AGC031")
    elif n == 32:
        print("AGC032")
    elif n == 33:
        print("AGC033")
    elif n == 34:
        print("AGC034")
    elif n == 35:
        print("AGC035")
    elif

=======
Suggestion 9

def main():
    n = int(input())
    if n < 10:
        print('AGC00%d' % n)
    elif n < 100:
        print('AGC0%d' % n)
    else:
        print('AGC%d' % n)
