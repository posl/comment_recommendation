Synthesizing 10/10 solutions

=======
Suggestion 1

def isLunLun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

=======
Suggestion 2

def main():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(K):
        x = lunlun[i]
        if x%10 != 0:
            lunlun.append(x*10 + x%10 - 1)
        lunlun.append(x*10 + x%10)
        if x%10 != 9:
            lunlun.append(x*10 + x%10 + 1)
    print(lunlun[K-1])

=======
Suggestion 3

def lunlun(n):
    if n < 10:
        return True
    d = n % 10
    n //= 10
    while n > 0:
        if abs(n % 10 - d) > 1:
            return False
        d = n % 10
        n //= 10
    return True

=======
Suggestion 4

def  lunlun( n ):
    q = [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ]
    for  i  in  range( n -  1 ):
        x = q.pop( 0 )
        d = x %  10 
        if  d >  0 :
            q.append( 10 * x + d -  1 )
        q.append( 10 * x + d )
        if  d <  9 :
            q.append( 10 * x + d +  1 )
     return  x

=======
Suggestion 5

def lunlun(x):
    for i in range(len(x)-1):
        if abs(int(x[i+1])-int(x[i]))>1:
            return False
    return True

=======
Suggestion 6

def solve():
    K = int(input())
    ans = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        for j in range(10):
            if ans[i]%10 == 0:
                if j == 0:
                    ans.append(ans[i]*10 + j)
                else:
                    ans.append(ans[i]*10 + j)
                    ans.append(ans[i]*10 + j - 1)
            elif ans[i]%10 == 9:
                if j == 9:
                    ans.append(ans[i]*10 + j)
                else:
                    ans.append(ans[i]*10 + j)
                    ans.append(ans[i]*10 + j + 1)
            else:
                ans.append(ans[i]*10 + j)
                ans.append(ans[i]*10 + j - 1)
                ans.append(ans[i]*10 + j + 1)
            ans.sort()
            if len(ans) >= K:
                break
    print(ans[K-1])

solve()

=======
Suggestion 7

def solve(K):
    # write your code in Python 3.6
    import heapq
    q = []
    for i in range(1,10):
        heapq.heappush(q, i)
    for i in range(K-1):
        v = heapq.heappop(q)
        if v%10 != 0:
            heapq.heappush(q, 10*v+(v%10)-1)
        heapq.heappush(q, 10*v+(v%10))
        if v%10 != 9:
            heapq.heappush(q, 10*v+(v%10)+1)
    return heapq.heappop(q)

=======
Suggestion 8

def main():
    n = int(input())
    lunlun_num = [i for i in range(1, 10)]
    for i in range(n):
        lunlun_num.append(lunlun_num[i]*10+lunlun_num[i]%10)
        if lunlun_num[i]%10 != 0:
            lunlun_num.append(lunlun_num[i]*10+lunlun_num[i]%10-1)
        if lunlun_num[i]%10 != 9:
            lunlun_num.append(lunlun_num[i]*10+lunlun_num[i]%10+1)
    lunlun_num.sort()
    print(lunlun_num[n-1])

=======
Suggestion 9

def  solve ( k ): 
     lunlun_numbers  =  [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ] 
     if  k  <=  len ( lunlun_numbers ): 
         return  lunlun_numbers [ k - 1 ] 
     while  k  >  len ( lunlun_numbers ): 
         new_lunlun_numbers  =  [] 
         for  i  in  range ( len ( lunlun_numbers )): 
             lunlun_number  =  lunlun_numbers [ i ] 
             last_digit  =  lunlun_number  %  10 
             if  last_digit  >  0 : 
                 new_lunlun_numbers . append ( lunlun_number  *  10  +  last_digit  -  1 ) 
             new_lunlun_numbers . append ( lunlun_number  *  10  +  last_digit ) 
             if  last_digit  <  9 : 
                 new_lunlun_numbers . append ( lunlun_number  *  10  +  last_digit  +  1 ) 
         lunlun_numbers  =  new_lunlun_numbers 
     return  lunlun_numbers [ k - 1 ]

=======
Suggestion 10

def lunlun(n):
    if n < 10:
        return [n]
    else:
        a = []
        for i in range(1, 10):
            a.extend(lunlun(i*10+n%10-1))
            a.extend(lunlun(i*10+n%10))
            a.extend(lunlun(i*10+n%10+1))
        return a

n = int(input())
a = []
for i in range(1, 10):
    a.extend(lunlun(i))
a.sort()
print(a[n-1])
