def main():
    L = int(input())
    # 1 から L+1 までの頂点を用意
    # 1 から頂点 i までのパスの長さは i-1
    # 1 から頂点 i までのパスの数は L-i+1
    # 1 から頂点 i までのパスの数が 1 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-1 以下
    # 1 から頂点 i までのパスの数が 2 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-2 以下
    # 1 から頂点 i までのパスの数が 3 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-3 以下
    # ...
    # 1 から頂点 i までのパスの数が L-i+1 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1) 以下
    # 1 から頂点 i までのパスの数が L-i+1 未満の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1)-1 以下
    # 1 から頂点 i までのパスの数が 0 の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1)-1 以下
    # 1 から頂点 i までのパスの数が 1 の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1)-1-1 以下
    # 1
