def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # compute
    ans = 1
    nums = [A, B, C, D, E]
    for i in range(5):
        for j in range(i+1, 5):
            if nums[i] == nums[j]:
                break
            elif j == 4:
                ans += 1
    # output
    print(ans)
