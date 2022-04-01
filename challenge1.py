from http.client import FOUND

from matplotlib import use


account=input('entre the account and i will give u enfo about u \n--> ')


at_char=account.find('@')
username=account[:at_char]
print(f'the user name is : {username}')

dot_char=account.find('.')
company_name=account[at_char+1:dot_char]
print(f'the company name is : {company_name}')

org_name=account[dot_char+1:]
print(f'the organiztion name is : {org_name}')

