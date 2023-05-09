def dice(a,b):
  for i in range(1,a+1):
    for j in range(1,a+1):
      if i+j == b:
        return 'Yes'
  return 'No'
a,b = map(int,input().split())
print(dice(a,b))

if __name__ == '__main__':
    dice()