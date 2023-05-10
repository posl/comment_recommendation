def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans_list = [0] * (2*n+1)
    ans_list[1] = 0
    for i in range(n):
        ans_list[2*i+2] = i+1
        ans_list[2*i+3] = i+1
    for i in range(2*n-1, 0, -1):
        ans_list[i//2] = ans_list[i] + 1
    for ans in ans_list:
        print(ans)
