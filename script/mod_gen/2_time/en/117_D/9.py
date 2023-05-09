def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    # Kの各bitについて、Aのbitが立っている数を数える
    # 1. そのbitが立っている数がN/2より大きい場合、そのbitは0になる
    # 2. そのbitが立っている数がN/2より小さい場合、そのbitは1になる
    # 3. そのbitが立っている数がN/2の場合、そのbitはKのbitによって決まる
    # 3-1. Kのbitが0の場合、そのbitは0になる
    # 3-2. Kのbitが1の場合、そのbitは1になる
    # 3-3. Kのbitが0の場合、そのbitは1になる
    # 1. 2. については、bitが立っている数を数えるだけで良い
    # 3. については、bitが立っている数がN/2の場合、そのbitはKのbitによって決まる
    # 3-1. 3-2. については、bitが立っている数を数えるだけで良い
    # 3-3. については、bitが立っている数がN/2の場合、そのbitは1になる
    # bitが立っている数を数える
    bit_count = [0] * 64
    for a in A:
        for i in range(64):
            if a & (1 << i):
                bit_count[i] += 1
    # bitが立っている数がN/2より大きい場合、そのbitは0になる
    # bitが立っている数がN/2より小さい場合、そのbitは1になる
    # bit

if __name__ == '__main__':
    solve()