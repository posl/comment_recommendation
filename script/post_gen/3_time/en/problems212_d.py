Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 1 <= Q <= 2 * 10^5
    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # All values in input are integers.
    # There is one or more i such that P_i=3.
    # If P_i=3, the bag contains at least one ball just before the i-th operation.
    Q = int(input())
    # 1 <= Q <= 2 * 10^5
    assert 1 <= Q <= 2 * 10**5
    bag = []
    add = 0
    for _ in range(Q):
        query = input().split()
        # 1 <= P_i <= 3
        assert 1 <= int(query[0]) <= 3
        if int(query[0]) == 1:
            # 1 <= X_i <= 10^9
            assert 1 <= int(query[1]) <= 10**9
            bag.append(int(query[1]) - add)
        elif int(query[0]) == 2:
            # 1 <= X_i <= 10^9
            assert 1 <= int(query[1]) <= 10**9
            add += int(query[1])
        else:
            # 1 <= X_i <= 10^9
            assert 1 <= min(bag) <= 10**9
            print(min(bag) + add)
            bag.remove(min(bag))

=======
Suggestion 2

def main():
    from heapq import heappush, heappop
    Q = int(input())
    que = []
    offset = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(que, query[1] - offset)
        elif query[0] == 2:
            offset += query[1]
        else:
            print(heappop(que) + offset)

=======
Suggestion 3

def main():
    import bisect
    q = int(input())
    a = []
    b = []
    for i in range(q):
        p, x = map(int, input().split())
        if p == 1:
            bisect.insort(a, x)
        elif p == 2:
            b.append(x)
        else:
            print(a[0] + sum(b))
            a.pop(0)
    return

=======
Suggestion 4

def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input().split())
    bag = []
    add = 0
    for query in queries:
        if query[0] == "1":
            bag.append(int(query[1]) - add)
        elif query[0] == "2":
            add += int(query[1])
        else:
            print(min(bag) + add)
            bag.remove(min(bag))

=======
Suggestion 5

def main():
    import sys
    from heapq import heappush, heappop
    input = sys.stdin.readline
    
    Q = int(input())
    q = []
    for _ in range(Q):
        p, x = map(int, input().split())
        heappush(q, (p, x))
    
    bag = []
    add = 0
    while q:
        p, x = heappop(q)
        if p == 1:
            heappush(bag, x - add)
        elif p == 2:
            add += x
        else:
            print(heappop(bag) + add)
    
    return

=======
Suggestion 6

def main():
    from heapq import heappop, heappush
    import sys
    input = sys.stdin.readline

    Q = int(input())
    heap = []
    ans = []
    offset = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(heap, query[1] - offset)
        elif query[0] == 2:
            offset += query[1]
        else:
            ans.append(heappop(heap) + offset)
    print(*ans, sep='

')
    return

=======
Suggestion 7

def main():
    Q = int(input())
    # 3 <= Q <= 2*10^5
    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # 1 <= i <= Q
    # P_i = 3
    # P_i = 3, bag contains at least one ball
    # 1 X_i
    # 2 X_i
    # 3

    # 1. Write an integer X_i on a blank ball and put it in the bag.
    # 2. For each ball in the bag, replace the integer written on it with that integer plus X_i.
    # 3. Pick up the ball with the smallest integer in the bag (if there are multiple such balls, pick up one of them). Record the integer written on this ball and throw it away.

    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # 1 <= i <= Q
    # P_i = 3
    # 1 X_i
    # 2 X_i
    # 3

    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # 1 <= i <= Q
    # P_i = 3
    # 1 X_i
    # 2 X_i
    # 3

    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # 1 <= i <= Q
    # P_i = 3
    # 1 X_i
    # 2 X_i
    # 3

    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # 1 <= i <= Q
    # P_i = 3
    # 1 X_i
    # 2 X_i
    # 3

    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # 1 <= i <= Q
    # P_i = 3
    # 1 X_i
    # 2 X_i
    # 3

    # 1 <= P_i <= 3
    # 1

=======
Suggestion 8

def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input().split())
    #print(queries)
    bag = []
    for i in range(Q):
        if queries[i][0] == '1':
            bag.append(int(queries[i][1]))
        elif queries[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(queries[i][1])
        elif queries[i][0] == '3':
            print(min(bag))
            bag.remove(min(bag))
        #print(bag)
        
    return

=======
Suggestion 9

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(input().split())

    #print(query)

    bag = []
    add = 0

    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]) - add)
        elif query[i][0] == '2':
            add += int(query[i][1])
        else:
            bag.sort()
            print(bag[0] + add)
            bag.pop(0)

=======
Suggestion 10

def main():
    Q = int(input())
    sum = 0
    min = 10**9
    min_list = []
    for i in range(Q):
        input_list = input().split()
        if input_list[0] == '1':
            sum += int(input_list[1])
        elif input_list[0] == '2':
            sum += int(input_list[1])
            min += int(input_list[1])
        else:
            min_list.append(min)
            min = 10**9
    for i in min_list:
        print(i+sum)
