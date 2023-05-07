def main():
    #This is the main function. It will be called when the program is run.
    #It will call the other functions to do the actual work.
    #It will return the answer to the calling function.
    #It will print the answer to the console.
    N, K, A = get_input()
    answer = solve(N, K, A)
    print(answer)
    return answer

if __name__ == '__main__':
    main()