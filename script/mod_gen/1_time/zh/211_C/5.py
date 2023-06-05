def main():
    # 读入字符串
    s = input()
    # 计数
    count = 0
    # 遍历字符串
    for i in range(len(s)):
        # 如果当前字符是c
        if s[i] == "c":
            # 遍历剩下的字符串
            for j in range(i+1,len(s)):
                # 如果当前字符是h
                if s[j] == "h":
                    # 遍历剩下的字符串
                    for k in range(j+1,len(s)):
                        # 如果当前字符是o
                        if s[k] == "o":
                            # 遍历剩下的字符串
                            for l in range(k+1,len(s)):
                                # 如果当前字符是k
                                if s[l] == "k":
                                    # 遍历剩下的字符串
                                    for m in range(l+1,len(s)):
                                        # 如果当前字符是u
                                        if s[m] == "u":
                                            # 遍历剩下的字符串
                                            for n in range(m+1,len(s)):
                                                # 如果当前字符是d
                                                if s[n] == "d":
                                                    # 遍历剩下的字符串
                                                    for o in range(n+1,len(s)):
                                                        # 如果当前字符是a
                                                        if s[o] == "a":
                                                            # 遍历剩下的字符串
                                                            for p in range(o+1,len(s)):
                                                                # 如果当前字符是i
                                                                if s[p] == "i":
                                                                    # 计数+1
                                                                    count += 1
    # 打印结果
    print(count % (10**9+7))

if __name__ == '__main__':
    main()