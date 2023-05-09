def follow_check(follow, a, b)
  if follow[a] == nil
    return false
  else
    if follow[a].include?(b)
      return true
    else
      return false
    end
  end
end

if __name__ == '__main__':
    follow_check()