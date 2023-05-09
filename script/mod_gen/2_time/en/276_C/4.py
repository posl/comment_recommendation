def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = []
    for i in range(n):
        q.append(p[i])
    q.sort()
    for i in range(n):
        if q[i] == p[i]:
            continue
        else:
            for j in range(i+1, n):
                if q[i] == p[j]:
                    p[i], p[j] = p[j], p[i]
                    break
    for i in range(n):
        if i == n-1:
            print(p[i])
        else:
            print(p[i], end=' ')
main()
I solved this problem by sorting the given permutation and comparing it with the original permutation. The first element that is different between the two permutations is the one that needs to be moved. I then moved it to the next element that is different between the two permutations, and so on until I found a position where the element could be moved.

if __name__ == '__main__':
    main()