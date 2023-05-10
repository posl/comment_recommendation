def main():
    S = input()
    result = 'Yes'
    box = ''
    for i in range(len(S)):
        if S[i] == '(':
            pass
        elif S[i] == ')':
            j = i - 1
            while True:
                if j < 0:
                    result = 'No'
                    break
                if S[j] == '(':
                    break
                j -= 1
            box = box[:j] + box[i:]
        else:
            if S[i] in box:
                result = 'No'
                break
            box += S[i]
    if box != '':
        result = 'No'
    print(result)

if __name__ == '__main__':
    main()