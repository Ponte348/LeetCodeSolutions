class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {
            'M' : 1000,
            'CM' : 900,
            'D' : 500,
            'CD' : 400,
            'C' : 100,
            'XC' : 90,
            'L' : 50,
            'XL' : 40,
            'X' : 10,
            'IX' : 9,
            'V' : 5,
            'IV' : 4,
            'I' : 1
        }

        integer = 0

        while s != "":
            if conversions.get(s[:2])!=None:
                integer+=conversions[s[:2]]
                s=s[2:]
            else:
                integer+=conversions[s[0]]
                s=s[1:]
                
        return integer