class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = re.sub(r"[.]","[.]",address)
        return a
