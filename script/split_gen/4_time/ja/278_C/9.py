def follow(x, y, user)
  if user[x] == nil
    user[x] = []
  end
  user[x] << y
end
