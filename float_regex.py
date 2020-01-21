import re

decimal_in_string = "hello float 12.9292 122212.32323 .456"

regex_d = r'\d*[.]\d*'

print(re.findall(regex_d,decimal_in_string))
