def get_input():
    input_str = input("请输入N M Q：")
    input_list = input_str.split(" ")
    N = int(input_list[0])
    M = int(input_list[1])
    Q = int(input_list[2])
    print("N M Q = ",N,M,Q)
    L = []
    R = []
    for i in range(M):
        input_str = input("请输入L R：")
        input_list = input_str.split(" ")
        L.append(int(input_list[0]))
        R.append(int(input_list[1]))
    p = []
    q = []
    for i in range(Q):
        input_str = input("请输入p q：")
        input_list = input_str.split(" ")
        p.append(int(input_list[0]))
        q.append(int(input_list[1]))
    return N,M,Q,L,R,p,q

if __name__ == '__main__':
    get_input()