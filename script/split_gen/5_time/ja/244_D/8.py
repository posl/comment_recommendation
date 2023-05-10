def main():
    # data load
    input_data = input()
    input_data = input_data.split()
    S1 = input_data[0]
    S2 = input_data[1]
    S3 = input_data[2]
    input_data = input()
    input_data = input_data.split()
    T1 = input_data[0]
    T2 = input_data[1]
    T3 = input_data[2]
    # data check
    #print(S1)
    #print(S2)
    #print(S3)
    #print(T1)
    #print(T2)
    #print(T3)
    # count check
    cnt_r = 0
    cnt_g = 0
    cnt_b = 0
    cnt_r += S1.count("R")
    cnt_r += S2.count("R")
    cnt_r += S3.count("R")
    cnt_g += S1.count("G")
    cnt_g += S2.count("G")
    cnt_g += S3.count("G")
    cnt_b += S1.count("B")
    cnt_b += S2.count("B")
    cnt_b += S3.count("B")
    #print(cnt_r)
    #print(cnt_g)
    #print(cnt_b)
    # result
    if cnt_r == 1 and cnt_g == 1 and cnt_b == 1:
        print("Yes")
    else:
        print("No")
