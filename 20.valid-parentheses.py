#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # c = []
        # for char in s:
        #     if char in ("(", "[", "{"):
        #         c.append(char)
        #         print(c)
        #     elif char[-1] == "(" and char == ")":
        #         c.pop()
        #     elif char[-1] == "[" and char == "]":
        #         c.pop()
        #     elif char[-1] == "{" and char == "}":
        #         c.pop()
        #     else:
        #         return False
        
        # if len(c) == 0:
        #     return 
        #     True
        while len(s) > 0:
            temp = s
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
            if temp == s:
                return False
        return True
        
# @lc code=end

