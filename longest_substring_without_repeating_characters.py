
def longest_substring_without_repeating_characters(text) -> int:
  seen = set()
  p1 = 0
  max_length = 0

  for p2 in range(len(text)):
    while text[p2] in seen:
      seen.remove(text[p1])
      p1 += 1
    seen.add(text[p2])
    max_length = max(max_length, p2 - p1 + 1)

  return max_length


if __name__ == '__main__':
  print(longest_substring_without_repeating_characters("abcabcbbz")) #* 3
  print(longest_substring_without_repeating_characters("jdkafnlcdsalkxcmpoiuytfccv")) #* 15
  print(longest_substring_without_repeating_characters("bbbbb")) #* 1
  print(longest_substring_without_repeating_characters("pwwkew")) #* 3
  print(longest_substring_without_repeating_characters("au")) #* 2
