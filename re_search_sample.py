import re

sample_data = "Today's new update means that you can finally add @Pizza Cat to" \
              "your @Retweet with comments! Learn more about this ne… " \
              "https://t.co/Rbc9TF2s5X"

sample_data_list = sample_data.split(' ') #string to list

print([w for w in sample_data_list if re.search('@[A-Za-z0-9_]+',w)])


'''
re logic below. 
'@[A-Za-z0-9_]+'

@==> starts with @
[A-Za-z0-9_]==> after @ any thing in between A-Z / a-z / 0-9 / _

+ ==> means one or more time can accure 

'''
