def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    pos = 0
    pos_list = [0]
    for i in range(K):
        pos = A[pos] - 1
        if pos in pos_list:
            break
        else:
            pos_list.append(pos)
    if i == K - 1:
        print(pos + 1)
    else:
        print(pos_list[(K - 1) % (i + 1) + 1] + 1)

if __name__ == '__main__':
    main()