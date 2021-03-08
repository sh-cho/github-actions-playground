import re


class Something:
    def __init__(self):
        self.aaa = re.search("(?<=abc)def", "abcdef")
