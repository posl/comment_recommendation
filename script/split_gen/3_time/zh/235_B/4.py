def solution(h):
    h.append(0)
    ans = 0
    stack = []
    for i in range(len(h)):
        if len(stack) == 0:
            stack.append(i)
        else:
            while len(stack) > 0 and h[stack[-1]] > h[i]:
                tmp = stack.pop()
                if len(stack) == 0:
                    ans = max(ans, h[tmp] * i)
                else:
                    ans = max(ans, h[tmp] * (i - stack[-1] - 1))
            stack.append(i)
    return ans
