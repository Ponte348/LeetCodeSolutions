class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        final = []
        keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        if len(digits)==1:
            return [letter for letter in keyboard[digits]]

        if len(digits)==2:
            for n in range(len(digits)):
                for m in range(n+1, len(digits)):
                    
                    for letter in keyboard[digits[n]]:
                        for other in keyboard[digits[m]]:
                            final.append(letter+other)

        if len(digits)==3:
            for n in range(len(digits)):
                for m in range(n+1, len(digits)):
                    for p in range(m+1, len(digits)):
                        
                        for letter in keyboard[digits[n]]:
                            for other in keyboard[digits[m]]:
                                for otherother in keyboard[digits[p]]:
                                    final.append(letter+other+otherother)
        
        if len(digits)==4:
            for n in range(len(digits)):
                for m in range(n+1, len(digits)):
                    for p in range(m+1, len(digits)):
                        for y in range(p+1, len(digits)):

                            for letter in keyboard[digits[n]]:
                                for other in keyboard[digits[m]]:
                                    for otherother in keyboard[digits[p]]:
                                        for otherotherother in keyboard[digits[y]]:
                                            final.append(letter+other+otherother+otherotherother)
        
        return final