def main():
    # N, M = list(map(int, input().split()))
    # A = []
    # for i in range(N):
    #     A.append(list(map(int, input().split()))[1:])
    # print(len(set.intersection(*map(set, A))))
    N, M = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    print(len(set.intersection(*map(set, A))))
