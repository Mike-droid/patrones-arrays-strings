from collections import Counter
from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    # Initialize the result list
    result = []

    # Get the length of the pattern
    p_len = len(p)

    # Create a counter for the pattern
    p_counter = Counter(p)

    # Create a counter for the current window in the string
    s_counter = Counter()

    for i in range(len(s)):
        # Add the current character to the window
        s_counter[s[i]] += 1

        # Remove the character that is left out of the window
        if i >= p_len:
            if s_counter[s[i - p_len]] == 1:
                del s_counter[s[i - p_len]]
            else:
                s_counter[s[i - p_len]] -= 1

        # Compare window counter to the pattern counter
        if s_counter == p_counter:
            result.append(i - p_len + 1)

    return result

# Example usage
if __name__ == '__main__':
    print(findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
    print(findAnagrams("abab", "ab"))         # Output: [0, 1, 2]


#* Example 1:
#* Input: s = "cbaebabacd", p = "abc"
#* Output: [0,6]
#* Explanation:
#* The substring with start index = 0 is "cba", which is an anagram of "abc".
#* The substring with start index = 6 is "bac", which is an anagram of "abc".

#* Example 2:
#* Input: s = "abab", p = "ab"
#* Output: [0,1,2]
#* Explanation:
#* The substring with start index = 0 is "ab", which is an anagram of "ab".
#* The substring with start index = 1 is "ba", which is an anagram of "ab".
#* The substring with start index = 2 is "ab", which is an anagram of "ab".
