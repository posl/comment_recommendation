def main():
    A,B,Q = map(int,input().split())
    s = [0]*A
    t = [0]*B
    x = [0]*Q
    for i in range(A):
        s[i] = int(input())
    for i in range(B):
        t[i] = int(input())
    for i in range(Q):
        x[i] = int(input())
    for i in range(Q):
        #print("x[i] = ",x[i])
        #print("s = ",s)
        #print("t = ",t)
        #print("x[i] = ",x[i])
        s.append(x[i])
        t.append(x[i])
        s.sort()
        t.sort()
        #print("s = ",s)
        #print("t = ",t)
        #print("x[i] = ",x[i])
        s_index = s.index(x[i])
        t_index = t.index(x[i])
        #print("s_index = ",s_index)
        #print("t_index = ",t_index)
        #print("s[s_index-1] = ",s[s_index-1])
        #print("t[t_index-1] = ",t[t_index-1])
        #print("s[s_index] = ",s[s_index])
        #print("t[t_index] = ",t[t_index])
        #print("s[s_index+1] = ",s[s_index+1])
        #print("t[t_index+1] = ",t[t_index+1])
        s_minus = 0
        t_minus = 0
        s_plus = 0
        t_plus = 0
        if s_index > 0:
            s_minus = s[s_index-1]
        if t_index > 0:
            t_minus = t[t_index-1]
        if s_index < A:
            s_plus = s[s_index+1]
        if t_index < B:
            t_plus = t[t_index+1]
        #print("s_minus = ",s_minus)
        #print("t_minus = ",t_minus)
        #print("s_plus = ",s_plus)
        #print("t_plus = ",t_plus)
        s_minus_t_minus = abs(s_minus-t_minus)
        s_minus_t = abs(s_minus-x[i])
        s_minus_t_plus = abs(s_minus-t_plus)
        s

if __name__ == '__main__':
    main()