class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result += str(len(word))+ "#"+word
        return result

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i=0
        while i < (len(s)):
            j= s.index('#', i)
            lenght= int(s[i:j])
            i= j+1
            decoded_list.append(s[i:i+lenght])
            i+= lenght
        return decoded_list
