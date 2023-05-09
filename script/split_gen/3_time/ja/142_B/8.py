def main():
    input_line1 = input()
    input_line2 = input()
    input_line1_split = input_line1.split()
    input_line2_split = input_line2.split()
    input_line1_split_int = [int(x) for x in input_line1_split]
    input_line2_split_int = [int(x) for x in input_line2_split]
    
    n = input_line1_split_int[0]
    k = input_line1_split_int[1]
    
    count = 0
    for i in range(n):
        if input_line2_split_int[i] >= k:
            count += 1
    
    print(count)
