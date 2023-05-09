def main():
    n, m = map(int, input().split())
    # 2人のおもちゃの情報を取得
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(m):
        c_i, d_i = map(int, input().split())
        c.append(c_i)
        d.append(d_i)
    # 2人のおもちゃが同じ形であるかどうかを判定
    # 2人のおもちゃが同じ形であるとは、以下の条件を満たす数列 P が存在することをいいます。
    # P は (1, ..., N) を並べ替えて得られる。
    # 任意の 1 以上 N 以下の整数 i, j に対し、以下が成り立つ。
    # 高橋君のおもちゃにおいてボール i, j がひもで繋がれていることと、青木君のおもちゃにおいてボール P_i, P_j がひもで繋がれていることは同値である。
    # 高橋君のおもちゃのボールの組み合わせを列挙
    ab = []
    for i in range(m):
        ab.append((a[i], b[i]))
    # 青木君のおもちゃのボールの組み合わせを列挙
    cd = []
    for i in range(m):
        cd.append((c[i], d[i]))
    # 高橋君のおもちゃのボールの組み合わせを列挙
    ab = []
    for i in range(m):
        ab.append((a[i], b[i]))
    # 青木君のおもちゃの
