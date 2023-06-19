def main():
    #H行和W列的白色方形单元格
    #h行和w列
    #还会剩下多少个白色单元格？
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W - h*W - w*H + h*w)
