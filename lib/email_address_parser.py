import re

class EmailAddressParser:
    def __init__(self, addresses = ""):
        self.addresses = addresses

    def parse(self):
        valid_pattern = re.compile(r'[a-z]+\.*[a-z]+@[a-z]+\.[a-z]+')
        valid_list = valid_pattern.findall(self.addresses)
        return sorted(valid_list)
    
# recommended to use split method... i had written a valid pattern and a split pattern 
# but was unable to use both once the string converted to a list after the first method
# looks like it's possible to do without split method, but for future i did include 
# while "" in split_list: split_list.remove("") to remove leftover empty strings from split method