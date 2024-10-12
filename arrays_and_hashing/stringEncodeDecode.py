# String Encode and Decode
# Solved 
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            for c in s:
                ret += str(ord(c)) + ','
            ret += ':'
        return ret

    def decode(self, s: str) -> List[str]:
        res = []
        l = s.split(":")[:-1]
        print(l)
        for i in l:
            new = ""
            print(i.split(","))
            for c in i.split(","):
                print(c)
                if (len(c) > 0):
                    new += chr(int(c,10))
            res.append(new)
        return res

