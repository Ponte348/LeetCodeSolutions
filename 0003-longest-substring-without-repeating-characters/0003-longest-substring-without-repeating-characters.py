class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final, sequence = "", ""
        for i in range(len(s)):
            sequence = s[i]

            for letter in s[i+1:]:
                if letter in sequence:
                    if len(sequence)>len(final):
                        final = sequence
                    break
                    
                sequence+=letter

            if len(sequence)>len(final):
                final = sequence

        return len(final)
        