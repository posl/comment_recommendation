def main():
    #Get input
    A, B, C = map(int, input().split())
    
    #Check for multiples
    for i in range(A, B+1):
        if i%C == 0:
            print(i)
            return
    #If no multiples
    print(-1)
