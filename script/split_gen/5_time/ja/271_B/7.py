def main():
    n, q = map(int, input().split())
    nums = []
    for i in range(n):
        nums.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(nums[s - 1][t - 1])
