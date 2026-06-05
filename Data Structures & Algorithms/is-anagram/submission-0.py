class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

               # Count characters in string s
        for char in s:
            map_s[char] = map_s.get(char, 0) + 1 
        
               # Count characters in string t
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1
        
               # Compare counts
        for key in map_s:
               # If the count doesn't match, it's not an anagram
            if map_s[key] != map_t.get(key, 0):
                return False
        return True