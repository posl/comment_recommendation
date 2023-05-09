def f(x): #define f(x)
    return x*x + 2*x + 3 #return the value of f(x)
t = int(input()) #input t
print(f(f(f(t)+t)+f(f(t)))) #print the value of f(f(f(t)+t)+f(f(t)))

if __name__ == '__main__':
    f()