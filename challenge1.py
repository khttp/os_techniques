from http.client import FOUND

from matplotlib import use


account=input('entre the account and i will give u enfo about u \n--> ')

username=account[:account.find('@')]
print(f'the user name is : {username}')

company_name=account[account.find('@')+1:account.find('.')]
print(f'the company name is : {company_name}')

org_name=account[account.find('.')+1:]
print(f'the organiztion name is : {org_name}')


