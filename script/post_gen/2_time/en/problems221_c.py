Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = input()
    if len(N) == 2:
        print(int(N[0]) * int(N[1]))
    else:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:])))

main()

=======
Suggestion 2

def main():
    N = int(input())
    N = str(N)
    l = len(N)
    if l == 2:
        print(int(N[0]) * int(N[1]))
    elif l == 3:
        print(max(int(N[0]) * int(N[1]) * int(N[2]), int(N[0]) * int(N[1] + N[2]), int(N[0] + N[1]) * int(N[2])))
    else:
        print(max(int(N[0]) * int(N[1]) * int(N[2]) * int(N[3]), int(N[0]) * int(N[1]) * int(N[2] + N[3]), int(N[0]) * int(N[1] + N[2]) * int(N[3]), int(N[0] + N[1]) * int(N[2]) * int(N[3]), int(N[0]) * int(N[1] + N[2] + N[3]), int(N[0] + N[1]) * int(N[2] + N[3]), int(N[0] + N[1] + N[2]) * int(N[3])))

=======
Suggestion 3

def main():
    n = input()
    l = len(n)
    if l == 2:
        print(max(int(n[0])*int(n[1]), int(n[1])*int(n[0])))
    else:
        print(max(int(n[0])*(int(''.join(n[1:]))), (int(''.join(n[:l-1])))*(int(n[l-1]))))

=======
Suggestion 4

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort(reverse=True)
    if N[0] == 1:
        print((N[0]+N[1]) * int("".join(map(str, N[2:]))))
    else:
        print(N[0] * int("".join(map(str, N[1:]))))

=======
Suggestion 5

def main():
  n = input()
  if len(n) == 2:
    print(int(n))
    return
  if n.count('0') == len(n) - 1:
    print('0')
    return
  if n.count('0') == len(n) - 2:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 3:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 4:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 5:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 6:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 7:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 8:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 9:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 10:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 11:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 12:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 13:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 14:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 15:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 16:
    print(int(n.replace('0', '')))
    return
  if n.count('0') == len(n) - 17:
    print(int(n.replace('0', '')))
    return
  if n.count('

=======
Suggestion 6

def main():
    N = input()
    #print(N)
    Nlen = len(N)
    #print(Nlen)
    #print(N[0])
    #print(N[1])
    #print(N[2])
    #print(N[3])
    #print(N[4])
    #print(N[5])
    #print(N[6])
    #print(N[7])
    #print(N[8])
    #print(N[9])
    #print(N[10])
    #print(N[11])
    #print(N[12])
    #print(N[13])
    #print(N[14])
    #print(N[15])
    #print(N[16])
    #print(N[17])
    #print(N[18])
    #print(N[19])
    #print(N[20])
    #print(N[21])
    #print(N[22])
    #print(N[23])
    #print(N[24])
    #print(N[25])
    #print(N[26])
    #print(N[27])
    #print(N[28])
    #print(N[29])
    #print(N[30])
    #print(N[31])
    #print(N[32])
    #print(N[33])
    #print(N[34])
    #print(N[35])
    #print(N[36])
    #print(N[37])
    #print(N[38])
    #print(N[39])
    #print(N[40])
    #print(N[41])
    #print(N[42])
    #print(N[43])
    #print(N[44])
    #print(N[45])
    #print(N[46])
    #print(N[47])
    #print(N[48])
    #print(N[49])
    #print(N[50])
    #print(N[51])
    #print(N[52])
    #print(N[53])
    #print(N[54])
    #print(N[55])
    #print(N[56])
    #print(N[57])
    #print(N[58])
    #print(N[59])
    #print(N[60])
    #print(N[61])
    #print(N[62])
    #print(N[63])
    #print(N[64])
    #print(N[65])
    #print(N[66])
    #print(N[67

=======
Suggestion 7

def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    N = ''.join(N)
    N = int(N)
    N = str(N)
    N = list(N)
    N = [int(x) for x in N]
    a = N[0]
    for i in range(1,len(N)):
        a = a*10 + N[i]
    b = N[0]
    for i in range(1,len(N)):
        b = b + N[i]*10**(i)
    print(a*b)

=======
Suggestion 8

def main():
    n = int(input())
    if n < 10:
        print(0)
        return
    n = str(n)
    n = list(n)
    n.sort(reverse=True)
    n = ''.join(n)
    print(int(n[0]) * int(n[1]))

=======
Suggestion 9

def main():
    #input
    N = input()
    #compute
    #output
    print(max(int(N[:-1]) * int(N[-1]), int(N[0]) * int(N[1:])))
