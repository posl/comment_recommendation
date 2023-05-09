def main():
    N = int(input())
    # 都市の数
    # 都市の数は都市の番号の最大値を示す
    # 都市の番号は1から始まるため、N+1としている
    # 都市の番号をそのままインデックスに使うため、N+2としている
    # 都市の数は、N+1番目のインデックスに格納されている
    # 都市の数は、N+2番目のインデックスに格納されている
    city = [0] * (N + 2)
    city[N + 1] = N
    city[N + 2] = 1
    # 都市の情報を保持するリスト
    # 都市の情報は、都市の番号をそのままインデックスに使う
    # 都市の情報は、都市の番号をそのままインデックスに使う
    city_info = [[] for i in range(N + 2)]
    # 道路の情報を保持するリスト
    # 道路の情報は、都市の番号をそのままインデックスに使う
    # 道路の情報は、都市の番号をそのままインデックスに使う
    road_info = [[] for i in range(N + 2)]
    for i in range(N - 1):
        A, B = map(int, input().split())
        # 道路の情報を保持するリスト
        # 道路の情報は、都市の番号をそのままインデックスに使う
        # 道路の情報は、都市の番号をそのままインデックスに使う
        road_info[A].append(B)
        road_info[B].append(A)
    # 都市の情報を保持するリスト
    # 都市の情報は、都市の番号をそのままインデックス
