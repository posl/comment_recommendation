def main():
    # 读入
    S = input()
    # 生成一个8个字符的字符串
    check_str = 'chokudai'
    # 计数
    count = 0
    # 从左到右遍历字符串
    for i in range(len(S)):
        # 如果当前字符是c
        if S[i] == check_str[0]:
            # 如果字符串长度大于8
            if len(S[i:]) >= 8:
                # 从左到右遍历字符串
                for j in range(i+1, len(S)):
                    # 如果当前字符是h
                    if S[j] == check_str[1]:
                        # 如果字符串长度大于8
                        if len(S[j:]) >= 7:
                            # 从左到右遍历字符串
                            for k in range(j+1, len(S)):
                                # 如果当前字符是o
                                if S[k] == check_str[2]:
                                    # 如果字符串长度大于8
                                    if len(S[k:]) >= 6:
                                        # 从左到右遍历字符串
                                        for l in range(k+1, len(S)):
                                            # 如果当前字符是k
                                            if S[l] == check_str[3]:
                                                # 如果字符串长度大于8
                                                if len(S[l:]) >= 5:
                                                    # 从左到右遍历字符串
                                                    for m in range(l+1, len(S)):
                                                        # 如果当前字符是u
                                                        if S[m] == check_str[4]:
                                                            # 如果字符串长度大于8
                                                            if len(S[m:]) >= 4:
                                                                # 从左到右遍历字符串
                                                                for n in range(m+1, len(S)):
                                                                    # 如果当前字符是d
                                                                    if S[n] == check_str[5]:
                                                                        # 如果字符串长度大于8
                                                                        if len(S[n:]) >= 3:
                                                                            # 从左到右遍历字符串
                                                                            for o in range(n+1, len(S)):
                                                                                # 如果当前字符是a
                                                                                if S[o] == check_str[6]:
                                                                                    # 如果字符串长度大于8
                                                                                    if len(S[o:]) >= 2:
                                                                                        # 从左到右遍历字符串
                                                                                        for p in range(o+1, len(S)):
