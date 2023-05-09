def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    dic = {}
    for i, a in enumerate(A):
        if a in dic:
            dic[a].append(i + 1)
            x = len(dic[a])
            B = dic[a]
            y = i + 1 - x
            C = [i + 1 for i in range(N) if i + 1 not in B]
            print('Yes')
            print(x, *B)
            print(y, *C)
            return
        else:
            dic[a] = [i + 1]
    print('No')

if __name__ == '__main__':
    main()