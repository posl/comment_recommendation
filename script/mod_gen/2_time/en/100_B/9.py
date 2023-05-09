def main():
  # Read the input
  D, N = map(int, input().split())
  # Calculate the result
  if N == 100:
    N = 101
  result = N * 100 ** D
  # Print the result
  print(result)
main()

if __name__ == '__main__':
    main()