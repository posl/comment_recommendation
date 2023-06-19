def triangle_num(num_list):
    num_list.sort()
    num_list.reverse()
    #print(num_list)
    count = 0
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            for k in range(j+1, len(num_list)):
                if num_list[i] < num_list[j] + num_list[k]:
                    count += 1
                else:
                    break
    return count

if __name__ == '__main__':
    triangle_num()