def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 余りを数える
    mod200 = [0 for _ in range(200)]
    for a in A:
        mod200[a % 200] += 1
    
    # 余りが同じものの組み合わせを数える
    ans = 0
    for m in mod200:
        ans += m * (m - 1) // 2
    print(ans)
