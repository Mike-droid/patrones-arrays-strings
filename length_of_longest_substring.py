def lengthOfLongestSubstring(s: str) -> int:
  inicio = 0
  caracteresAPosicion = {}
  mayorLongtiud = 0

  for fin in range(len(s)):
    if s[fin] in caracteresAPosicion and inicio <= caracteresAPosicion[s[fin]]:
      inicio = caracteresAPosicion[s[fin]] + 1
    caracteresAPosicion[s[fin]] = fin
    mayorLongtiud = max(mayorLongtiud, fin - inicio + 1)
  return mayorLongtiud


print(lengthOfLongestSubstring("abcabcbbz")) #* 3
print(lengthOfLongestSubstring("jdkafnlcdsalkxcmpoiuytfccv")) #* 15
print(lengthOfLongestSubstring("bbbbb")) #* 1
print(lengthOfLongestSubstring("pwwkew")) #* 3
print(lengthOfLongestSubstring("au")) #* 2
