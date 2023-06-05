def get_max_xor_sum(n,k,a_list):
    #a_list.sort(reverse=True)
    a_list.sort()
    a_list.reverse()
    #print(a_list)
    max_xor_sum = 0
    for i in range(0,n):
        xor_sum = 0
        for j in range(0,n):
            xor_sum += a_list[j] ^ a_list[i]
        if xor_sum > max_xor_sum:
            max_xor_sum = xor_sum
    return max_xor_sum

if __name__ == '__main__':
    get_max_xor_sum()