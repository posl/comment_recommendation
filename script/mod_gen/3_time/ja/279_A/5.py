def main():
    S = input()
    stack = []
    count = 0
    for i in range(len(S)):
        if len(stack) == 0:
            stack.append(S[i])
        elif stack[-1] == S[i]:
            stack.append(S[i])
        else:
            stack.pop()
            count += 1
    print(count)

if __name__ == '__main__':
    main()