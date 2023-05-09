def main():
    # 三角形の辺の長さ
    ab, bc, ca = map(int, input().split())
    # 三角形の面積
    area = (ab * bc) // 2
    print(area)

if __name__ == '__main__':
    main()