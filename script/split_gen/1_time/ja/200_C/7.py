def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    #print(A)
    dict = {}
    for a in A:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1
    #print(dict)
    ans = 0
    for d in dict:
        ans += dict[d] * (dict[d] - 1) // 2
    print(ans)
