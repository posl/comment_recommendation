def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    a_sum = sum([a for a, _ in ab])
    b_sum = sum([b for _, b in ab])
    ab_diff = [(a - b) for a, b in ab]
    ab_diff.sort(reverse=True)
    if a_sum < b_sum:
        print(0)
        exit()
    diff_sum = 0
    for i in range(n):
        diff_sum += ab_diff[i]
        if diff_sum >= 0:
            print(i + 1)
            exit()
