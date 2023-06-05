def main():
    n = int(input())
    #序列长度为key,序列为value
    seq_dict = {}
    #序列长度为key,序列数量为value
    seq_len_dict = {}
    for i in range(n):
        seq = list(map(int, input().split()))[1:]
        seq_len = len(seq)
        if seq_len in seq_dict:
            if seq not in seq_dict[seq_len]:
                seq_dict[seq_len].append(seq)
                seq_len_dict[seq_len] += 1
        else:
            seq_dict[seq_len] = []
            seq_dict[seq_len].append(seq)
            seq_len_dict[seq_len] = 1
    result = 0
    for value in seq_len_dict.values():
        result += value
    print(result)

if __name__ == '__main__':
    main()