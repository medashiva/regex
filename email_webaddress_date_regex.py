import re


date1 = '21-01-2020 dsfdsafds 22-01-2020'

#print(re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}',date1))

'''
\d ==> digit [0-9]
\d{2} == > 2 digits '21-01-2020' , so first 21 is two digit one
[/-]==>  it means the separator can be / or -


follows for month and year
'''

email1 = "apple@gmail.com  shiva@gmail.com shiva@hai"


email_regex = '\S+@\S+[.]\S+'

#print(re.findall(regex,email1))


website_address = "www.googsss111le.comsadsada hello gmail.com"

website_address2 = 'http://example.com'

web_regex = '^(?:http|https)://?\S+[.]\S+'

website_address3 = "https://www.geeksforgeeks.org/introduction-to-project-lombok-in-java-and-how-to-get-started/"

print(re.findall(web_regex,website_address3))

