def main():
  N = int(input())
  for i in range(1,10):
    if N%i == 0:
      if N//i <= 9:
        print("Yes")
        return
  print("No")
  return
