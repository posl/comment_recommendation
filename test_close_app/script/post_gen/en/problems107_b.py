Synthesizing 10/10 solutions

=======

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    h = [True] * H
    w = [True] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                break
        else:
            h[i] = False
    for j in range(W):
        for i in range(H):
            if a[i][j] == "#":
                break
        else:
            w[j] = False
    for i in range(H):
        if h[i]:
            print("".join(a[i][j] for j in range(W) if w[j]))

=======

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    B = []
    for i in range(H):
        if '#' in A[i]:
            B.append(A[i])
    C = []
    for j in range(W):
        if any([B[i][j] == '#' for i in range(len(B))]):
            C.append(j)
    for i in range(len(B)):
        for j in C:
            print(B[i][j], end='')
        print()

main()

=======

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = [0] * W
    c = [0] * H
    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                b[j] = 1
                c[i] = 1
    for i in range(H):
        if c[i] == 0:
            continue
        for j in range(W):
            if b[j] == 1:
                print(a[i][j], end="")
        print()

=======

def main():
    H, W = map(int, input().split())
    A = [list(input()) for i in range(H)]
    B = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] == '#':
                B[i][j] = 1
    for j in range(W):
        if sum([B[i][j] for i in range(H)]) == 0:
            for i in range(H):
                B[i][j] = -1
    for i in range(H):
        if sum([B[i][j] for j in range(W)]) == 0:
            for j in range(W):
                B[i][j] = -1
    for i in range(H):
        for j in range(W):
            if B[i][j] == 1:
                print(A[i][j], end='')
        if sum([B[i][j] for j in range(W)]) > 0:
            print()

main()

=======

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    A = list(map(list, zip(*A)))
    A = [a for a in A if '#' in a]
    A = list(map(list, zip(*A)))
    for a in A:
        print(''.join(a))

=======

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    B = []
    for i in range(W):
        if '#' in [A[j][i] for j in range(H)]:
            B.append(i)
    for i in range(H):
        if '#' in A[i]:
            print(''.join([A[i][j] for j in B]))
    return

main()

=======

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    # row
    h = []
    for i in range(H):
        if "#" in A[i]:
            h.append(i)

    # column
    w = []
    for j in range(W):
        if "#" in [A[i][j] for i in range(H)]:
            w.append(j)

    # output
    for i in h:
        print("".join([A[i][j] for j in w]))

main()

=======

def main():
    #Read input
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    #Delete white rows
    a = [row for row in a if "#" in row]
    #Delete white columns
    a = [row for row in zip(*a) if "#" in row]
    #Transpose back
    a = zip(*a)
    #Print
    for row in a:
        print("".join(row))

main()

H, W = map(int, input().split())
a = [input() for _ in range(H)]
a = [row for row in a if "#" in row]
a = [row for row in zip(*a) if "#" in row]
a = zip(*a)
for row in a:
    print("".join(row))

a = [input() for _ in range(H)]

a = [row for row in a if "#" in row]

a = [row for row in zip(*a) if "#" in row]

a = zip(*a)

for row in a:

print("".join(row))

a = [input() for _ in range(H)]

a = [row for row in a if "#" in row]

a = [row for row in zip(*a) if "#" in row]

a = zip(*a)

for row in a:

print("".join(row))

a = [input() for _ in range(H)]

a = [row for row in a if "#" in row]

a = [row for row in zip(*a) if "#" in row]

a = zip(*a)

for row in a:

print("".join(row))

a = [input() for _ in range(H)]

a = [row for row in a if "#" in row]

a = [row for row in zip(*a) if "#" in row]

a = zip(*a)

for row in a:

print("".join(row))

a = [input() for _ in range(H)]

a = [row for row in a if "#" in row]

a = [row for row in zip(*a) if "#" in row]

a = zip(*a)

for row in a:

print("".join(row))

a = [input() for _ in range(H)]

a = [row for row in a if "#" in row]

a = [row for row in zip(*a) if "#" in row]

a

=======

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][j] == '.' else 1 for j in range(W)] for i in range(H)]

    # 0: not black, 1: black
    a = [[0 if a[i][

=======

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    # 行列を転置して、列ごとに処理
    A = list(map(list, zip(*A)))

    # 一旦、削除する列を格納するリストを用意
    del_col = []

    # 列ごとに、処理
    for i in range(W):
        # 一旦、削除する列を格納するリストを用意
        del_col = []
        # 行ごとに、処理
        for j in range(H):
            # .が含まれている場合、
            if A[i][j] == '.':
                # その列を削除するリストに追加
                del_col.append(j)

        # 一旦、削除する列を格納するリストを用意
        del_col = []
        # 行ごとに、処理
        for j in range(H):
            # .が含まれている場合、
            if A[i][j] == '.':
                # その列を削除するリストに追加
                del_col.append(j)

        # 一旦、削除する列を格納するリストを用意
        del_col = []
        # 行ごとに、処理
        for j in range(H):
            # .が含まれている場合、
            if A[i][j] == '.':
                # その列を削除するリストに追加
                del_col.append(j)

        # 一旦、削除する列を格納するリストを用意
        del_col = []
        # 行ごとに、処理
        for j in range(H):
            # .が含まれている場合、
            if A[i][j] == '.':
                # その列を削除するリストに追加
                del_col.append(j)

        # 一旦、削除する列を格納するリストを
