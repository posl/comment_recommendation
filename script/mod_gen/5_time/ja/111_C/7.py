def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    even_dic = {}
    odd_dic = {}
    for i in range(n//2):
        if even[i] in even_dic:
            even_dic[even[i]] += 1
        else:
            even_dic[even[i]] = 1
        if odd[i] in odd_dic:
            odd_dic[odd[i]] += 1
        else:
            odd_dic[odd[i]] = 1
    even_dic = sorted(even_dic.items(), key=lambda x: x[1], reverse=True)
    odd_dic = sorted(odd_dic.items(), key=lambda x: x[1], reverse=True)
    if even_dic[0][0] == odd_dic[0][0]:
        if len(even_dic) == 1 and len(odd_dic) == 1:
            print(n//2)
        elif len(even_dic) == 1:
            print(n//2 - odd_dic[1][1])
        elif len(odd_dic) == 1:
            print(n//2 - even_dic[1][1])
        else:
            print(n//2 - max(even_dic[1][1] + odd_dic[0][1], even_dic[0][1] + odd_dic[1][1]))
    else:
        print(n//2 - even_dic[0][1] - odd_dic[0][1])

if __name__ == '__main__':
    main()