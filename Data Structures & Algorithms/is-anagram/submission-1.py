class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for word in s:
            s_dict[word] = s_dict.get(word, 0) + 1
        for word in t:
            t_dict[word] = t_dict.get(word, 0) + 1

        return s_dict == t_dict