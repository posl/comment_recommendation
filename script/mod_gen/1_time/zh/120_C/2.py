def main():
    S = input()
    #print(S)
    #print(type(S))
    #print(len(S))
    #print(S[0])
    #从左到右依次遍历，如果是0则入栈，如果是1则出栈，如果出栈的时候栈为空则将结果+1
    stack = []
    result = 0
    for i in range(len(S)):
        if S[i] == '0':
            stack.append(S[i])
        else:
            if len(stack) == 0:
                result += 1
            else:
                stack.pop()
    #从右到左依次遍历，如果是1则入栈，如果是0则出栈，如果出栈的时候栈为空则将结果+1
    stack = []
    for i in range(len(S)-1, -1, -1):
        if S[i] == '1':
            stack.append(S[i])
        else:
            if len(stack) == 0:
                result += 1
            else:
                stack.pop()
    print(result)

if __name__ == '__main__':
    main()