class Solution:

    def encode(self, strs: List[str]) -> str:
        # str -> {len(str)}#{str}
        encoded_strs = []
        for original_str in strs:
            encoded_strs.append(f"{len(original_str)}#{original_str}")
        return "".join(encoded_strs)
    
    def get_len_str(self, pos, s):
        len_chars = []
        while pos < len(s) and s[pos].isnumeric():
            len_chars.append(s[pos])
            pos += 1
        return "".join(len_chars)
    
    def decode(self, s: str) -> List[str]:
        pos = 0
        strs = []
        while pos < len(s):
            len_str = self.get_len_str(pos, s)
            pos += len(len_str) + 1
            word_len = int(len_str)
            word = s[pos:pos+word_len]
            pos += len(word)
            strs.append(word)
        return strs

    