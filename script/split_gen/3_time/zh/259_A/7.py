def main():
    # 读取输入
    # 输入的所有数值都是整数
    N, M, X, T, D = map(int, input().split())
    # 求高桥在第M个生日时的身高，单位是厘米。
    # 从第X岁生日开始，到第N岁生日结束，身高每年增加D厘米
    # 高桥在第M个生日时的身高，单位是厘米
    # 高桥出生时身高至少有1厘米
    # 身高在第X个生日和第N个生日之间没有变化
    # 所以，高桥在第M个生日时的身高，单位是厘米 = 高桥在第X个生日时的身高，单位是厘米 + (M-X)*D厘米
    # 高桥在第X个生日时的身高，单位是厘米 = T厘米 + (X-1)*D厘米
    # 所以，高桥在第M个生日时的身高，单位是厘米 = T厘米 + (X-1)*D厘米 + (M-X)*D厘米
    # 所以，高桥在第M个生日时的身高，单位是厘米 = T厘米 + (M-1)*D厘米
    # 所以，高桥在第M个生日时的身高，单位是厘米 = T厘米 + M*D厘米 - D厘米
    # 所以，高桥在第M个生日时的身高，单位是厘米 = (T-D)厘米 + M*D厘米
    # 所以，高桥在第M个生日时的身高，单位是厘米 = (T-D)厘米 + M*D厘米
    # 所以，高桥在第M个生日时的身高，单位是厘米 = (T+(M-1)*D
