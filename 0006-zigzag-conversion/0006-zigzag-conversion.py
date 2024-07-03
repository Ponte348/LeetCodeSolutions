class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for n in range(numRows)]

        while s!="":
            for i in range(numRows):
                if s=="":
                    break
                rows[i].append(s[0])
                s=s[1:]

            for j in range(numRows-2, 0, -1):
                if s=="":
                    break
                rows[j].append(s[0])
                s=s[1:]

        return "".join(sum(rows, []))