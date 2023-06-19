def main():
    n,k=map(int,input().split())
    candy=list(map(int,input().split()))
    candy_set=set(candy)
    candy_set_len=len(candy_set)
    if candy_set_len<k:
        print(candy_set_len)
        return
    candy_dict={}
    for i in range(k):
        if candy[i] not in candy_dict:
            candy_dict[candy[i]]=1
        else:
            candy_dict[candy[i]]+=1
    max_len=len(candy_dict)
    for i in range(k,n):
        candy_dict[candy[i-k]]-=1
        if candy_dict[candy[i-k]]==0:
            del candy_dict[candy[i-k]]
        if candy[i] not in candy_dict:
            candy_dict[candy[i]]=1
        else:
            candy_dict[candy[i]]+=1
        if max_len<len(candy_dict):
            max_len=len(candy_dict)
    print(max_len)

if __name__ == '__main__':
    main()