def function(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s = int(input())
a = [s]
i = 1
while True:
    if function(a[i-1]) in a:
        print(i+1)
        break
    else:
        a.append(function(a[i-1]))
    i+=1

if __name__ == '__main__':
    function()