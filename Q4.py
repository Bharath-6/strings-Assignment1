def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('bharath', 0))
print(remove_char('bharath', 2))
print(remove_char('bharath', 5))
