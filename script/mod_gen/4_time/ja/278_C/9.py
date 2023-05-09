def follow(x, y, user)
  if user[x] == nil
    user[x] = []
  end
  user[x] << y
end

if __name__ == '__main__':
    follow()