def main():
    #N 両編成の列車があります。
    #この列車の前から i 両目は、後ろから何両目でしょうか？
    N, i = map(int, input().split())
    #1 ≦ N ≦ 100
    #1 ≦ i ≦ N
    #答えを出力せよ。
    print(N - i + 1)
