Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for i, cut in enumerate(cuts):
                if cut == x:
                    print(cuts[i + 1] - cuts[i])
                    break

=======
Suggestion 2

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for i in range(len(cut)):
                if cut[i] == x:
                    print(cut[i+1] - cut[i])
                    break

=======
Suggestion 3

def main():
    L, Q = map(int, input().split())
    x = [0] * Q
    c = [0] * Q
    for i in range(Q):
        c[i], x[i] = map(int, input().split())
    piece = []
    piece.append((1, L))
    for i in range(Q):
        if c[i] == 1:
            for j in range(len(piece)):
                if x[i] >= piece[j][0] and x[i] <= piece[j][1]:
                    piece.append((piece[j][0], x[i]))
                    piece.append((x[i], piece[j][1]))
                    del piece[j]
                    break
        else:
            for j in range(len(piece)):
                if x[i] >= piece[j][0] and x[i] <= piece[j][1]:
                    print(piece[j][1]-piece[j][0])
                    break

=======
Suggestion 4

def main():
    L, Q = map(int, input().split())
    cuts = []
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            left = 0
            right = len(cuts)
            while left < right:
                mid = (left + right) // 2
                if cuts[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            if left % 2 == 0:
                print(x - cuts[left - 1])
            else:
                print(cuts[left] - x)

=======
Suggestion 5

def main():
    L, Q = map(int, input().split())
    Lst = [L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            Lst.append(x)
            Lst.append(L - x)
            Lst.sort()
        else:
            for j in range(len(Lst)):
                if Lst[j] >= x:
                    print(Lst[j])
                    break

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    tree = [L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            tree.append(x)
            tree.append(L - x)
            tree.sort()
        else:
            for i in range(len(tree)):
                if tree[i] >= x:
                    print(tree[i])
                    break

main()

=======
Suggestion 7

def main():
    L,Q = map(int, input().split())
    cut = [0 for _ in range(L)]
    cut[0] = 1
    cut[L-1] = 1
    for _ in range(Q):
        c,x = map(int, input().split())
        if c == 1:
            cut[x-1] = 1
        else:
            left = x-1
            right = x-1
            while left >= 0 and cut[left] == 0:
                left -= 1
            while right < L and cut[right] == 0:
                right += 1
            print(right-left)

=======
Suggestion 8

def main():
    L, Q = map(int, input().split())
    #L: length of timber
    #Q: number of queries
    #c_i: 1 or 2 (1 <= i <= Q)
    #x_i: 1 <= x_i <= L - 1 (1 <= i <= Q)
    #for c_i = 1, 2, it is guaranteed that there will have been no cut at Mark x_i when the query is to be processed.
    #All values in input are integers.
    #At the time of the first query, no cut has been made, so the piece with Mark 2 has a length of 5 meters. Thus, you should print 5.
    #In the second query, the piece is cut into two pieces with lengths of 3 and 2 meters.
    #At the time of the third query, the piece with Mark 2 has a length of 3 meters, so you should print 3.  
    #In the j-th line, print the response to the j-th such query.

    #L: length of timber
    #Q: number of queries
    #c_i: 1 or 2 (1 <= i <= Q)
    #x_i: 1 <= x_i <= L - 1 (1 <= i <= Q)
    #for c_i = 1, 2, it is guaranteed that there will have been no cut at Mark x_i when the query is to be processed.
    #All values in input are integers.
    #At the time of the first query, no cut has been made, so the piece with Mark 2 has a length of 5 meters. Thus, you should print 5.
    #In the second query, the piece is cut into two pieces with lengths of 3 and 2 meters.
    #At the time of the third query, the piece with Mark 2 has a length of 3 meters, so you should print 3.  
    #In the j-th line, print the response to the j-th such query.
    #print(L, Q)
    #print("c_i, x_i")
    #for i in range(Q):
    #    c_i, x_i = map(int, input().split())
    #    print(c_i, x_i)

    #print(L, Q)
    #print("c_i

=======
Suggestion 9

def main():
    L, Q = map(int, input().split())
    # Initialize the list of pieces of timber
    pieces = [(0, L)]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            # Cut the piece at Mark x into two
            pieces = cut(pieces, x)
        else:
            # Print the length of the piece with Mark x
            print(length(pieces, x))

=======
Suggestion 10

def main():
    L, Q = map(int, input().split())
    #Initialize the list with the length of L
    L_list = [L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            #If c = 1, cut the piece at Mark x into two
            L_list.append(x)
            L_list.append(L-x)
            L_list.sort()
        else:
            #If c = 2, choose the piece with Mark x on it and print its length
            for j in range(len(L_list)):
                if L_list[j] >= x:
                    print(L_list[j])
                    break
