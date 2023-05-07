def main():
    n = int(input())
    v = list(map(int, input().split()))
    
    even = v[::2]
    odd = v[1::2]
    
    even_dic = {}
    odd_dic = {}
    
    for i in even:
        if i in even_dic:
            even_dic[i] += 1
        else:
            even_dic[i] = 1
    
    for i in odd:
        if i in odd_dic:
            odd_dic[i] += 1
        else:
            odd_dic[i] = 1
    
    even_max = max(even_dic, key=even_dic.get)
    odd_max = max(odd_dic, key=odd_dic.get)
    
    if even_max == odd_max:
        even_max_num = even_dic[even_max]
        odd_max_num = odd_dic[odd_max]
        
        del even_dic[even_max]
        del odd_dic[odd_max]
        
        even_max2 = max(even_dic, key=even_dic.get)
        odd_max2 = max(odd_dic, key=odd_dic.get)
        
        even_max2_num = even_dic[even_max2]
        odd_max2_num = odd_dic[odd_max2]
        
        print(min(n - even_max2_num - odd_max_num, n - even_max_num - odd_max2_num))
    else:
        print(n - even_dic[even_max] - odd_dic[odd_max])

if __name__ == '__main__':
    main()