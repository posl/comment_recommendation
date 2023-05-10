def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K, P)
    stack = []
    for i in range(N):
        #print(i)
        while stack and P[stack[-1]] >= P[i]:
            stack.pop()
        if stack:
            print(stack[-1] + 1)
        else:
            print(-1)
        stack.append(i)
