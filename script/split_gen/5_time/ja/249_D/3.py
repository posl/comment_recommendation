def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 1 <= i, j, k <= n
    # a[i] / a[j] = a[k]
    # a[i] = a[j] * a[k]
    # a[j] = a[i] / a[k]
    # a[k] = a[i] / a[j]
    # 1 <= a[i], a[j], a[k] <= 2 * 10^5
    # 1 <= a[j] * a[k] <= 4 * 10^10
    # 1 <= a[i] / a[k] <= 2 * 10^5
    # 1 <= a[i] / a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i