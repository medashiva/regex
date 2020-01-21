import re


hash_string = "hello @saipallavi  #rowdybaby @danush.. sample hashtag"

reg_hash = '^@\S+'


hash_string_l = hash_string.split(' ')

print([w for w in hash_string_l if re.search(reg_hash,w)])
