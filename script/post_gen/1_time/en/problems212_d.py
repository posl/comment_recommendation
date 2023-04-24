Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    bag = []
    for _ in range(Q):
        p, x = map(int, input().split())
        if p == 1:
            bag.append(x)
        elif p == 2:
            bag = [i + x for i in bag]
        else:
            bag = sorted(bag)
            print(bag.pop(0))

=======
Suggestion 2

def main():
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    bag = []
    for q in query:
        if q[0] == '1':
            bag.append(int(q[1]))
        elif q[0] == '2':
            for i in range(len(bag)):
                bag[i] += int(q[1])
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 3

def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    heap = []
    for q in query:
        if q[0] == 1:
            heapq.heappush(heap, q[1])
        elif q[0] == 2:
            heap = [x + q[1] for x in heap]
            heapq.heapify(heap)
        else:
            ans.append(heapq.heappop(heap))
    print(*ans, sep='
')
main()

=======
Suggestion 4

def main():
    import sys
    from heapq import heappush, heappop, heapify
    readline = sys.stdin.readline
    write = sys.stdout.write
    Q = int(readline())
    heap = []
    heapify(heap)
    add = 0
    for _ in range(Q):
        query = readline().split()
        if query[0] == '1':
            heappush(heap, int(query[1]) - add)
        elif query[0] == '2':
            add += int(query[1])
        else:
            write(str(heappop(heap) + add) + '

')
    return

=======
Suggestion 5

def main():
    import heapq
    q = int(input())
    a = []
    heap = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
            heapq.heappush(heap, query[1])
        elif query[0] == 2:
            for j in range(len(a)):
                a[j] += query[1]
            heapq.heappush(heap, heap[0]+query[1])
        else:
            print(heapq.heappop(heap))

main()

=======
Suggestion 6

def main():
    import heapq
    Q = int(input())
    balls = []
    h = []
    heapq.heapify(h)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(h, (query[1], i))
        elif query[0] == 2:
            balls.append((query[1], i))
        else:
            while len(h) > 0:
                if h[0][1] <= i - len(balls):
                    print(heapq.heappop(h)[0])
                    break
                else:
                    heapq.heappop(h)
    for i in range(len(balls)):
        if h[0][1] <= i:
            print(heapq.heappop(h)[0])
        else:
            heapq.heappop(h)

=======
Suggestion 7

def   main (): 
     import   sys 
     import   heapq 

     input   =   sys . stdin . readline 

     Q   =   int ( input ()) 
     heap   =   [] 
     sum   =   0 
     for   _   in   range ( Q ): 
         p ,   x   =   map ( int ,   input (). split ()) 
         if   p   ==   1 : 
             heapq . heappush ( heap ,   x   -   sum ) 
         elif   p   ==   2 : 
             sum   +=   x 
         else : 
             print ( heapq . heappop ( heap )   +   sum )

=======
Suggestion 8

def main():
    Q = int(input())
    queries = []

    for i in range(Q):
        queries.append(input().split())

    #print(queries)

    #print(queries[0][0])
    #print(queries[0][1])

    #print(queries[1][0])
    #print(queries[1][1])

    #print(queries[2][0])

    #print(queries[3][0])
    #print(queries[3][1])

    #print(queries[4][0])

    #print(queries[5][0])

    #print(queries[6][0])

    #print(queries[7][0])

    #print(queries[8][0])

    #print(queries[9][0])

    #print(queries[10][0])

    #print(queries[11][0])

    #print(queries[12][0])

    #print(queries[13][0])

    #print(queries[14][0])

    #print(queries[15][0])

    #print(queries[16][0])

    #print(queries[17][0])

    #print(queries[18][0])

    #print(queries[19][0])

    #print(queries[20][0])

    #print(queries[21][0])

    #print(queries[22][0])

    #print(queries[23][0])

    #print(queries[24][0])

    #print(queries[25][0])

    #print(queries[26][0])

    #print(queries[27][0])

    #print(queries[28][0])

    #print(queries[29][0])

    #print(queries[30][0])

    #print(queries[31][0])

    #print(queries[32][0])

    #print(queries[33][0])

    #print(queries[34][0])

    #print(queries[35][0])

    #print(queries[36][0])

    #print(queries[37][0])

    #print(queries[38][0])

    #print(queries[39][0])

    #print(queries[40][0])

    #print(queries[41][0])

    #print(queries[42][0])

    #print(queries[43][

=======
Suggestion 9

def main():
    q = int(input())
    a = []
    for i in range(q):
        a.append(list(map(int, input().split())))
    #print(a)
    #print(len(a))
    q = len(a)
    #print(q)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[8][0])
    #print(a[8][1])
    #print(a[9][0])
    #print(a[9][1])
    #print(a[10][0])
    #print(a[10][1])
    #print(a[11][0])
    #print(a[11][1])
    #print(a[12][0])
    #print(a[12][1])
    #print(a[13][0])
    #print(a[13][1])
    #print(a[14][0])
    #print(a[14][1])
    #print(a[15][0])
    #print(a[15][1])
    #print(a[16][0])
    #print(a[16][1])
    #print(a[17][0])
    #print(a[17][1])
    #print(a[18][0])
    #print(a[18][1])
    #print(a[19][0])
    #print(a[19][1])
    #print(a[20][0])
    #print(a[20][1])
    #print(a[21][0])
    #print(a[21][1])
    #print(a[22][0])
    #print(a[22][1])
    #print(a[23][0])
    #print(a[23][1])
    #print(a[24][0])
    #print(a[24][
