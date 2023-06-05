def main():
    #input
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    #process
    result = 0
    for i in range(n):
        result += a_list[i] * b_list[i]
    #output
    if result == 0:
        print('Yes')
    else:
        print('No')
