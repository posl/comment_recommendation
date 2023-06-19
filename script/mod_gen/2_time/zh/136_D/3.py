def main():
    input_str = input()
    input_len = len(input_str)
    output_list = [0] * input_len
    
    #print(input_str)
    #print(input_len)
    #print(output_list)
    
    #print(input_str[0])
    #print(input_str[1])
    #print(input_str[2])
    
    #print(input_str[input_len-3])
    #print(input_str[input_len-2])
    #print(input_str[input_len-1])
    
    for i in range(input_len):
        #print(i)
        if input_str[i] == 'R':
            for j in range(i+1,input_len):
                if input_str[j] == 'L':
                    output_list[j-1] += 1
                    break
        elif input_str[i] == 'L':
            for j in range(i,0,-1):
                if input_str[j-1] == 'R':
                    output_list[j] += 1
                    break
        else:
            print('error')
    
    #print(output_list)
    
    for i in range(input_len):
        print(output_list[i],end=' ')

if __name__ == '__main__':
    main()