def get_longest_acgt(s):
    acgt_list = []
    acgt_str = ''
    for i in range(len(s)):
        if s[i] in 'ACGT':
            acgt_str += s[i]
        else:
            if acgt_str != '':
                acgt_list.append(acgt_str)
                acgt_str = ''
    if acgt_str != '':
        acgt_list.append(acgt_str)
        acgt_str = ''
    return len(max(acgt_list, key=len))

if __name__ == '__main__':
    get_longest_acgt()