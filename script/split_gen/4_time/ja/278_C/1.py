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
