def main():
    # 读入数据
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    # 优惠券数目大于商品数目，直接返回0
    if k >= n:
        print(0)
        return
    # 对商品价格排序
    a.sort()
    # 优惠券最多使用k次，所以最多可以优惠k*x元
    # 如果优惠券最多可以优惠k*x元，那么就优惠掉最贵的k*x元商品
    # 剩下的商品价格之和就是最小价格
    print(sum(a[:n-k]) - k*x)

if __name__ == '__main__':
    main()