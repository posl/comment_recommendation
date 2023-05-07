def main():
    S = input()
    Q = int(input())
    t = []
    k = []
    for i in range(Q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    #print(S)
    #print(Q)
    #print(t)
    #print(k)
    #A → BC, B → CA, C → AB
    #S^{(i)} be the result of simultaneously replacing the characters of S^{(i-1)} as follows: A → BC, B → CA, C → AB.
    S_dict = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    S_dict_rev = {'BC': 'A', 'CA': 'B', 'AB': 'C'}
    #print(S_dict)
    #print(S_dict_rev)
    #S^{(i)} be the result of simultaneously replacing the characters of S^{(i-1)} as follows: A → BC, B → CA, C → AB.
    S_dict2 = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    S_dict2_rev = {'BC': 'A', 'CA': 'B', 'AB': 'C'}
    S_dict3 = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    S_dict3_rev = {'BC': 'A', 'CA': 'B', 'AB': 'C'}
    S_dict4 = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    S_dict4_rev = {'BC': 'A', 'CA': 'B', 'AB': 'C'}
    S_dict5 = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    S_dict5_rev = {'BC': 'A', 'CA': 'B', 'AB': 'C'}
    S_dict6 = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    S_dict6_rev = {'BC': 'A', 'CA': 'B', 'AB': 'C'}
    S_dict7 = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    S_dict7_rev = {'BC': 'A', 'CA': 'B', 'AB

if __name__ == '__main__':
    main()