def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        ci, ti = map(int, input().split())
        c.append(ci)
        t.append(ti)
    min_cost = 1001
    for i in range(N):
        if t[i] <= T:
            min_cost = min(min_cost, c[i])
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
main()
My code is here.
I have a question. I have a list of lists. I want to find the index of the smallest value in each list. For example, if I have a list of lists like this:
[[1, 2, 3], [2, 1, 3], [1, 3, 2]]
I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?
I have a list of lists. I want to find the index of the smallest value in each list. For example, if I have a list of lists like this:
[[1, 2, 3], [2, 1, 3], [1, 3, 2]]
I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?
I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?
I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?
I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?
I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?
I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?
I want to find the index

if __name__ == '__main__':
    main()