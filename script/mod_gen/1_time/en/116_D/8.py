def solve(N,K,topping,deliciousness):
    #print(N,K,topping,deliciousness)
    ans = 0
    for i in range(2**N):
        #print(i)
        #print(bin(i))
        #print(bin(i)[2:].zfill(N))
        #print(bin(i)[2:].zfill(N)[::-1])
        #print(bin(i)[2:].zfill(N)[::-1][:K])
        #print(bin(i)[2:].zfill(N)[::-1][K:])
        #print(bin(i)[2:].zfill(N)[::-1][:K].count('1'))
        #print(bin(i)[2:].zfill(N)[::-1][K:].count('1'))
        #print('---')
        if bin(i)[2:].zfill(N)[::-1][:K].count('1') == K:
            top = []
            deli = 0
            for j in range(N):
                if bin(i)[2:].zfill(N)[::-1][j]=='1':
                    top.append(topping[j])
                    deli += deliciousness[j]
            #print(top)
            #print(deli)
            #print(len(set(top)))
            #print(len(set(top))*len(set(top)))
            #print('---')
            if ans < deli + len(set(top))*len(set(top)):
                ans = deli + len(set(top))*len(set(top))
    return ans

if __name__ == '__main__':
    solve()