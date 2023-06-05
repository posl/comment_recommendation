Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    h,w,n = map(int,input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int,input().split())))
    for i in range(n):
        cards[i].append(i+1)
    cards.sort(key=lambda x:x[0])
    cards.sort(key=lambda x:x[1])
    for i in range(n):
        print(cards[i][2],cards[i][0],cards[i][1])

=======
Suggestion 3

def main():
    h,w,n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a1 = sorted(list(set(a)))
    b1 = sorted(list(set(b)))
    a2 = {}
    b2 = {}
    for i in range(len(a1)):
        a2[a1[i]] = i+1
    for i in range(len(b1)):
        b2[b1[i]] = i+1
    for i in range(n):
        print(a2[a[i]],b2[b[i]])

=======
Suggestion 4

def main():
    print('hello world')

=======
Suggestion 5

def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    #print(h,w,n)
    #print(a[0],b[0])
    #print(len(a),len(b))
    #print(a[0],b[0])
    #print(a[1],b[1])
    #print(a[2],b[2])
    #print(a[3],b[3])
    #print(a[4],b[4])
    #print(a[5],b[5])
    #print(a[6],b[6])
    #print(a[7],b[7])
    #print(a[8],b[8])
    #print(a[9],b[9])
    #print(a[10],b[10])
    #print(a[11],b[11])
    #print(a[12],b[12])
    #print(a[13],b[13])
    #print(a[14],b[14])
    #print(a[15],b[15])
    #print(a[16],b[16])
    #print(a[17],b[17])
    #print(a[18],b[18])
    #print(a[19],b[19])
    #print(a[20],b[20])
    #print(a[21],b[21])
    #print(a[22],b[22])
    #print(a[23],b[23])
    #print(a[24],b[24])
    #print(a[25],b[25])
    #print(a[26],b[26])
    #print(a[27],b[27])
    #print(a[28],b[28])
    #print(a[29],b[29])
    #print(a[30],b[30])
    #print(a[31],b[31])
    #print(a[32],b[32])
    #print(a[33],b[33])
    #print(a[34],b[34])
    #print(a[35],b[35])
    #print(a[36],b[36])
    #print(a[37

=======
Suggestion 6

def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(n):
        a[i] -= 1
        b[i] -= 1
    h1 = []
    w1 = []
    for i in range(n):
        h1.append(a[i])
        w1.append(b[i])
    h1 = list(set(h1))
    w1 = list(set(w1))
    h1.sort()
    w1.sort()
    h2 = {}
    w2 = {}
    for i in range(len(h1)):
        h2[h1[i]] = i
    for i in range(len(w1)):
        w2[w1[i]] = i
    for i in range(n):
        print(h2[a[i]]+1,w2[b[i]]+1)

=======
Suggestion 7

def main():
    H,W,N = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    #for i in range(N):
    #    for j in range(N):
    #        if A[i] == A[j] and B[i] == B[j]:
    #            print(i+1,j+1)
    #            break
    #        elif A[i] == A[j] and B[i] != B[j]:
    #            print(i+1,B[j])
    #            break
    #        elif A[i] != A[j] and B[i] == B[j]:
    #            print(A[j],j+1)
    #            break
    #        elif A[i] != A[j] and B[i] != B[j]:
    #            print(A[j],B[j])
    #            break
