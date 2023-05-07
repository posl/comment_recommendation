def main():
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]
    bridge = bridge[::-1]
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    for i in range(1, M):
        if bridge[i][0] < bridge[i][1]:
            bridge[i][0], bridge[i][1] = bridge[i][1], bridge[i][0]
        if bridge[i] == bridge[i - 1]:
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] - 1
    for i in range(M):
        print(ans[M - 1 - i])
main()
This is my submission.
This code is very slow.
I'm not sure why this code is slow.
I think this code is O(N + M).
I think this is a problem with the input.
I tried to make a list of the number of bridges that connect the island.
However, it was not possible to pass the test.
I think this code is O(N + M).
I think this is a problem with the input.
I tried to make a list of the number of bridges that connect the island.
However, it was not possible to pass the test.
This is my submission.
This code is very slow.
I'm not sure why this code is slow.
I think this code is O(N + M).
I think this is a problem with the input.
I tried to make a list of the number of bridges that connect the island.
However, it was not possible to pass the test.
I think this code is O(N + M).
I think this is a problem with the input.
I tried to make a list of the number of bridges that connect the island.
However, it was not possible to pass the test.
I think this code is O(N + M).
I think this is a problem with the input.
I tried to make a list of the number of bridges that connect the island.
However, it was not possible to pass the test.
I think this code is O(N + M).
I think this is a problem with the input.
I tried to make a list of the number of bridges that connect the island.
However, it was not possible to pass the test.
I think this code is
