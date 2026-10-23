class Solution:

    def encode(self, strs: List[str]) -> str:
        code=""
        for word in strs:
            slen=len(word)
            code=code+word+"ñ"
        return code 

    def decode(self, s: str) -> List[str]:
        code=""
        decoded=[]
        for letter in s:
            if letter == "ñ":
                decoded.append(code)
                code=""
            else:
                code= code+letter
        return decoded

