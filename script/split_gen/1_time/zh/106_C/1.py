def main():
    s = input()
    k = int(input())
    l = len(s)
    s = list(s)
    i = 0
    while i < k:
        if s[i] != '1':
            i += 1
        else:
            j = 0
            while j < k:
                if s[i + j] == '1':
                    j += 1
                else:
                    break
            if j == k:
                break
            else:
                i += j
    print(s[i])
main()
