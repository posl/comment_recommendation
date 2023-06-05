def main():
    #N = int(input())
    #name_list = []
    #for i in range(N):
    #    name_list.append(input().split())
    #name_list = [['tanaka', 'taro'], ['sato', 'hanako'], ['tanaka', 'taro']]
    name_list = [['sypdgidop', 'bkseq'], ['bajsqz', 'hh'], ['ozjekw', 'mcybmtt'], ['qfeysvw', 'dbo']]
    for i in range(len(name_list)):
        if name_list[i] in name_list[i+1:]:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()