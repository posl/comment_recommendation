def main():
    N, M = map(int, input().split())
    # 隣り合っている人のリストを作成
    people = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        people[A-1].append(B-1)
        people[B-1].append(A-1)
    # 隣り合っている人のリストの中で、最も長いものを探す
    # この長さが N-1 ならば、全ての条件を満たすことができる
    # そうでなければ、満たすことができない
    max_len = 0
    for p in people:
        if len(p) > max_len:
            max_len = len(p)
    if max_len == N-1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()