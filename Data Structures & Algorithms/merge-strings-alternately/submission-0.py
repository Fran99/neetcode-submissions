class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        k, j = 0, 0
        while True:
            if k < len(word1):
                output += word1[k]
                k += 1

            if j < len(word2):
                output += word2[j]
                j += 1
            if k >= len(word1) and j >= len(word2):
                break;        
        return output    