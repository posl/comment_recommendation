Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L = int(input())
    if L == 2:
        print(2,1)
        print(1,2,1)
        return
    if L == 3:
        print(3,2)
        print(1,2,0)
        print(2,3,1)
        return
    if L == 4:
        print(8,10)
        print(1,2,0)
        print(2,3,0)
        print(3,4,0)
        print(1,5,0)
        print(2,6,0)
        print(3,7,0)
        print(4,8,0)
        print(5,6,1)
        print(6,7,1)
        print(7,8,1)
        return
    if L == 5:
        print(5,7)
        print(1,2,0)
        print(2,3,1)
        print(3,4,0)
        print(4,5,0)
        print(2,4,0)
        print(1,3,3)
        print(3,5,1)
        return
    if L == 6:
        print(4,4)
        print(1,2,0)
        print(2,3,0)
        print(3,4,0)
        print(1,4,1)
        return
    if L == 7:
        print(5,6)
        print(1,2,0)
        print(2,3,0)
        print(3,4,0)
        print(4,5,0)
        print(1,3,1)
        print(3,5,1)
        return
    if L == 8:
        print(6,8)
        print(1,2,0)
        print(2,3,0)
        print(3,4,0)
        print(4,5,0)
        print(5,6,0)
        print(1,3,0)
        print(3,5,0)
        print(1,4,1)
        return
    if L == 9:
        print(7,8)
        print(1,2,0)
        print(2,3,0

=======
Suggestion 2

def main():
    L = int(input())
    if L == 2:
        print('2 1')
        print('1 2 1')
        return
    if L == 3:
        print('2 2')
        print('1 2 1')
        print('2 1 2')
        return
    if L == 4:
        print('8 10')
        print('1 2 0')
        print('2 3 0')
        print('3 4 0')
        print('1 5 0')
        print('2 6 0')
        print('3 7 0')
        print('4 8 0')
        print('5 6 1')
        print('6 7 1')
        print('7 8 1')
        return

    N = 1
    while L > 2:
        N += 1
        L -= 2
    M = N + (N - 1) * (N - 2) // 2
    print(N, M)
    for i in range(1, N + 1):
        print(i, i + 1, 0)
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            print(i, j, 1)

=======
Suggestion 3

def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    print(20, 60)
    for i in range(1, 20):
        print(i, i + 1, 0)
    for i in range(1, 20):
        print(i, i + 1, L - 1)
    for i in range(1, 20):
        print(i, i + 1, 2 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 3 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 4 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 5 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 6 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 7 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 8 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 9 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 10 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 11 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 12 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 13 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 14 * L - 1)
    for i in range(1, 20):
        print(i, i + 1, 15 * L - 1)
    for i in range(1, 20):
        print(i,

=======
Suggestion 4

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
        print(i, i + 1, 1)
    for i in range(N - 1):
        print(i + 1, i + 2, (L - 1) - i)
    for i in range(N - 1):
        print(i + 1, i + 2, (L - 1) + i)

=======
Suggestion 5

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(N-1):
        print(i+1, i+2, 0)
    for i in range(N-1):
        print(i+1, i+2, 1)
    for i in range(1, N-1):
        print(1, i+2, i+1)
    for i in range(N-2):
        print(i+2, i+3, 0)
    for i in range(N-2):
        print(i+2, i+3, 1)
    for i in range(1, N-2):
        print(1, i+3, i+2)
    for i in range(N-3):
        print(i+3, i+4, 0)
    for i in range(N-3):
        print(i+3, i+4, 1)
    for i in range(1, N-3):
        print(1, i+4, i+3)
    for i in range(N-4):
        print(i+4, i+5, 0)
    for i in range(N-4):
        print(i+4, i+5, 1)
    for i in range(1, N-4):
        print(1, i+5, i+4)
    for i in range(N-5):
        print(i+5, i+6, 0)
    for i in range(N-5):
        print(i+5, i+6, 1)
    for i in range(1, N-5):
        print(1, i+6, i+5)
    for i in range(N-6):
        print(i+6, i+7, 0)
    for i in range(N-6):
        print(i+6, i+7, 1)
    for i in range(1, N-6):
        print(1, i+7, i+6)
    for i in range(N-7):
        print(i+7, i+8, 0)
    for i in range(N-7):
        print(i+7, i+8, 1)
    for i in range(1, N-7):
        print(1

=======
Suggestion 6

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        print(i, i + 1, i)

    for i in range(1, N):
        for j in range(i + 2, N + 1):
            print(i, j, i * (j - i) + 1)

    for i in range(1, L + 1):
        print(i, i + 1, 0)

=======
Suggestion 7

def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N - 1):
        print(i, i + 2, 1)
    L -= 2
    for i in range(1, N - 1):
        if L == 0:
            break
        if L >= 2 ** (N - i - 1):
            print(i, i + 2, 2 ** (N - i - 2))
            L -= 2 ** (N - i - 1)
    for i in range(1, N - 1):
        if L == 0:
            break
        if L >= 2 ** (N - i - 1):
            print(i, i + 2, 2 ** (N - i - 2) + 1)
            L -= 2 ** (N - i - 1)

=======
Suggestion 8

def main():
    L = int(input())
    N = 2
    while 2**N <= L:
        N += 1
    M = N + L - 1
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(N-1):
        if L & 1:
            print(i+1, i+2, 2**(N-1-i))
        L >>= 1

=======
Suggestion 9

def main():
    #print('Hello World')
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, L-1)
    for i in range(1, N):
        print(i, i+1, i)
    for i in range(1, N):
        print(i, i+1, L-i)
    for i in range(1, N):
        print(i, i+1, L-i-1)

=======
Suggestion 10

def generate_graph(L):
    current_length = 0
    edge_length = 0
    edges = []
    for i in range(1, L):
        edges.append([i, i + 1, edge_length])
        current_length += edge_length
        edge_length += 1
        if current_length == L:
            break
        elif current_length > L:
            edge_length -= 1
            current_length -= edge_length
            for j in range(i - 1, 0, -1):
                edges.append([j, j + 1, edge_length])
                current_length += edge_length
                edge_length += 1
                if current_length == L:
                    break
                elif current_length > L:
                    edge_length -= 1
                    current_length -= edge_length
                    break
    return edges

L = int(input())
edges = generate_graph(L)
print(len(edges) + 1, len(edges))
for edge in edges:
    print(*edge)
print(len(edges) + 1, 1, 0)
