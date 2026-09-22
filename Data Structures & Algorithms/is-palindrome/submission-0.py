class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum()).lower()
        print(clean)
        stack = []

        k = len(clean) - 1
        while k >= 0:
            stack.append(clean[k])
            k -= 1
        res = "".join(stack)
        
        return res == clean
