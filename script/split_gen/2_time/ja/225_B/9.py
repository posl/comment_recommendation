def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1であることを確認する
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1でない場合、スターではない
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1である場合、スターかもしれない
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1である場合、
    # その頂点に隣接する頂点の数が2以上であればスターではない
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1である場合、
    # その頂点に隣接する頂点の数が2であればスターである
    
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1である場合、
    # その頂点に隣接する頂点の数が2であればスターである
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1である場合、
    # その頂点に隣接する頂点の数が2以上であればスターではない
    # 木の頂点数Nのうち、1つだけ隣接する頂点数がN-1である場合、スターかもしれない
    # 木の頂点数Nのうち、1つだけ隣接する頂
