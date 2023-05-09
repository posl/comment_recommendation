def main():
    a,b,k = map(int, input().split())
    nums = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            nums.append(i)
    print(nums[-k])
