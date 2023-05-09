def main():
    N, M = map(int, input().split())
    # 人数N, 舞踏会数M
    # print(N, M)
    # 人数分のリストを作成
    # 0は未参加、1は1回以上参加
    people = [0] * N
    # print(people)
    for i in range(M):
        # 舞踏会の出席者数
        K = int(input())
        # print(K)
        # 舞踏会に出席した人のリスト
        attend = list(map(int, input().split()))
        # print(attend)
        for j in range(K):
            # print(attend[j])
            # 出席者が1人でもいれば1
            people[attend[j] - 1] = 1
    # print(people)
    for i in range(N):
        if people[i] == 0:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()