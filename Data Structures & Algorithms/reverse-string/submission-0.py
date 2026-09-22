class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k = 0 # first pointer
        j = len(s) - 1 #last pointer

        while k < j:
            s[j], s[k] = s[k], s[j]
            k += 1
            j -= 1
        return s    
