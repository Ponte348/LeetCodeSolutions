class Solution:
    def myAtoi(self, s: str) -> int:
        final = ""
        negative = 0
        start = False  # To indicate if we have started to process the number

        for letter in s:
            if letter == " " and not start:
                continue
            if letter == "-" and not start:
                negative = 1
                start = True
                continue
            if letter == "+" and not start:
                start = True
                continue
            if not letter.isnumeric():
                break
            if letter.isnumeric():
                if final == "" and letter == "0":
                    start = True
                    continue
                final += letter
                start = True
        if final == "":
            return 0
        if negative:
            return max(int(final) * -1, -2**31)
        else:
            return min(int(final), 2**31-1)