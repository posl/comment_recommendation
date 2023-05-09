def main():
    s = input()
    result = [0] * len(s)
    r_count = 0
    l_count = 0
    r_index = []
    l_index = []
    for i in range(len(s)):
        if s[i] == 'R':
            r_count += 1
            r_index.append(i)
        else:
            l_count += 1
            l_index.append(i)
    for i in range(len(r_index)):
        if i == len(r_index)-1:
            result[r_index[i]] += r_count // 2 + r_count % 2
            result[r_index[i]+1] += r_count // 2
        else:
            result[r_index[i]] += r_count // 2
            result[r_index[i]+1] += r_count // 2 + r_count % 2
    for i in range(len(l_index)):
        if i == 0:
            result[l_index[i]] += l_count // 2 + l_count % 2
            result[l_index[i]-1] += l_count // 2
        else:
            result[l_index[i]] += l_count // 2
            result[l_index[i]-1] += l_count // 2 + l_count % 2
    print(*result)
