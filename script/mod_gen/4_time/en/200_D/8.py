def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200で割ったあまりの値をキーにして、その値が出現する位置をリストで保持する
    # あまりが0の場合は、その値が2回以上出現することはないので、
    # その場合は出現位置のリストの長さが2以上の場合に処理を行う
    # あまりが0以外の場合は、その値が2回以上出現することがあるので、
    # その場合は出現位置のリストの長さが1以上の場合に処理を行う
    mod = {}
    for i in range(N):
        m = A[i] % 200
        if m == 0:
            if m in mod and len(mod[m]) > 1:
                print('Yes')
                print(1, mod[m][0] + 1)
                print(1, mod[m][1] + 1)
                return
        else:
            if m in mod and len(mod[m]) > 0:
                print('Yes')
                print(1, mod[m][0] + 1)
                print(i + 1, end=' ')
                for j in range(N):
                    if j == mod[m][0]:
                        continue
                    print(j + 1, end=' ')
                print('')
                return
        if m in mod:
            mod[m].append(i)
        else:
            mod[m] = [i]
    print('No')

if __name__ == '__main__':
    main()