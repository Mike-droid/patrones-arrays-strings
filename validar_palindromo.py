def validar_palindromo(text: str)-> bool:
  if text[:] == text[::-1] :
    return True
  else:
    left, right = 0, len(text) -1

    while left < right:
      if text[left] != text[right]:
        skip_left, skip_right = text[left + 1 : right + 1], text[left : right]
        return (skip_left == skip_left[::-1] or skip_right == skip_right[::-1])
      left, right = left+1, right-1
      return True


if __name__ == '__main__':
  print(validar_palindromo("aba")) #* true
  print(validar_palindromo("abca")) #* true
  print(validar_palindromo("peep")) #* true
  print(validar_palindromo("peeps")) #* true
  print(validar_palindromo("speep")) #* true
  print(validar_palindromo("pesep")) #* true
  print(validar_palindromo("spesep")) #* true
  print(validar_palindromo("popeyes")) #* false
  print(validar_palindromo("qwe"))#* false
  print(validar_palindromo("hello"))#* false
