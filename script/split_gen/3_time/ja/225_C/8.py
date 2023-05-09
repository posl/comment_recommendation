def main():
    #入力
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    #N行M列の行列BがAから一部の矩形領域を切り出したものであるかを判定
    #Bの左上の座標を全て試す
    for i in range(10**100 - N + 1):
        for j in range(7 - M + 1):
            #Bの左上の座標が(i,j)の時、BがAから一部の矩形領域を切り出したものであるかを判定
            #Bの各要素がAの(i+x,j+y)と一致するかを判定
            for x in range(N):
                for y in range(M):
                    if B[x][y] != (i + x) * 7 + j + y + 1:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                return
    print("No")
    return
