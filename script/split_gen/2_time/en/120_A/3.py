def main():
    #get input
    A, B, C = map(int, input().split())
    #calculate answer
    answer = min(B // A, C)
    #print answer
    print(answer)
