def main():
    # 读取输入
    # 读取输入
    N, M = map(int, input().split())
    # 处理
    # 1. 偶数加偶数是偶数
    # 2. 奇数加奇数是偶数
    # 3. 偶数加奇数是奇数
    # 4. 奇数加偶数是奇数
    # 5. 偶数个数的球和奇数个数的球，两个球和为偶数的情况：偶数个数的球中选两个，奇数个数的球中选两个
    # 6. 偶数个数的球和奇数个数的球，两个球和为奇数的情况：偶数个数的球中选一个，奇数个数的球中选一个
    # 7. 偶数个数的球和奇数个数的球，两个球和为奇数的情况：偶数个数的球中选一个，奇数个数的球中选一个
    # 8. 偶数个数的球和奇数个数的球，两个球和为偶数的情况：偶数个数的球中选两个，奇数个数的球中选两个
    # 9. 两个球和为偶数的情况：偶数个数的球中选两个，奇数个数的球中选两个
    # 10. 两个球和为奇数的情况：偶数个数的球中选一个，奇数个数的球中选一个
    # 11. 两个球和为奇数的情况：偶数个数的球中选一个，奇数个数的球中选一个
    # 12. 两个球和为偶数的情况：偶数个数的球中选两个，奇数个数的
