def solve(n, k, p):
    # 从后往前遍历，如果当前的数比栈顶的数要大，就把栈顶的数弹出，直到当前的数比栈顶的数要小
    # 这样就可以保证栈内的数是从小到大排列的
    # 用一个栈来存储，栈内的数是从小到大排列的
    stack = []
    ans = [-1 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        # 如果当前的数比栈顶的数要大，就把栈顶的数弹出，直到当前的数比栈顶的数要小
        while len(stack) > 0 and stack[-1][0] < p[i]:
            # 弹出栈顶的数，弹出的数的下标就是当前数的答案
            _, index = stack.pop()
            ans[index] = i + 1
        # 把当前的数和下标入栈
        stack.append((p[i], i))
    return ans
