class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            temp_str = ''
            for j in range(length):
                temp_str += s[i]
                i += 1
            res.append(temp_str)
        return res