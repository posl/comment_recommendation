def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #昇順に並べ替えることができるかどうか
    #K個のグループに分けて、各グループで昇順に並べ替えることができるかどうか
    #K個のグループのうち、i番目のグループの中身は、
    #A[i], A[i+K], A[i+2K], A[i+3K], ... となる
    #グループの中身を昇順に並べ替えるには、
    #各グループの中身を一つのリストにまとめて、
    #そのリストを昇順に並べ替えればよい。
    #グループの数は、(N+K-1)//Kで求められる
    #グループの数が1の場合は、Aを昇順に並べ替えればよい
    #グループの数が2以上の場合は、
    #各グループの中身を一つのリストにまとめて、
    #そのリストを昇順に並べ替えることができるかどうかを調べる必要がある
    #各グループの中身を一つのリストにまとめる
    #各グループの中身を一つのリストにまとめるには、
    #グループの数が2以上の場合は、
    #各グループの中身を一つのリストにまとめて、
    #そのリストを昇順に並べ替えることができるかどうかを調
