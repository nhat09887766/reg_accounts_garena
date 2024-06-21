import requests,random
print(''':::::::::::::    ::::::   ::: 
:+:       :+:   :+: :+:   :+: 
+:+       +:+  +:+   +:+ +:+  
:#::+::#  +#++:++     +#++:   
+#+       +#+  +#+     +#+    
#+#       #+#   #+#    #+#    
###       ###    ###   ###    
''')
print('--------------------------------')
input_name=input('input username:')
input_email=input('input name email:')
input_sl=input('number of accounts:')
def reg_garena(input_name,input_email):
  name=str(input_name)+str(random.randint(1000,9999))
  email=str(input_email)+str(random.randint(1000,9999))
  headers={
    'Host': 'sso.garena.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'x-datadome-clientid': '3ZUXmCPo9C~DYJZFHq1EvFinxKOn188xFE4fgo-y6ED9cqo0WDWKmFau6GA_e7E44t4boLDha2FXfkuh6K~sR-wmwv0wBOiDHmb6DI4wgePBUGiKVY7JT8JHKHj~zOrP',
    'Origin': 'https://sso.garena.com',
    'Connection':'keep-alive',
    'Referer': 'https://sso.garena.com/universal/register?locale=en-SG',
    'Cookie': '_ga_1M7M9L6VPX=GS1.1.1692323423.3.1.1692323455.0.0.0; _ga=GA1.1.714292989.1692283076; datadome=3ZUXmCPo9C~DYJZFHq1EvFinxKOn188xFE4fgo-y6ED9cqo0WDWKmFau6GA_e7E44t4boLDha2FXfkuh6K~sR-wmwv0wBOiDHmb6DI4wgePBUGiKVY7JT8JHKHj~zOrP',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
  }
  payload={
    'username':name,
    'email':str(email)+'@gmail.com',
    'password':'9abb5122762c8659736fb8ec24b05b9c15709cd93c201f3416a8cf40cf4b6cb4a8dc129c556db15f5572c744085013a956c5210efaf8864b4ef7f89830e0a4ed1a02ec2a3b3ac82094372ed84626ebb27549af43dbde659fe364f45f91d34a5773ec1db23301585772b4eb794d3a421c527f86c9c0042924774836d2190b7dd5',
    'location':'SG',
    'mobile_no':'',
    'otp':'',
    'locale':'en-SG',
    'format':'json',
    'id':'1692323641860',
  }
  reg=requests.post('https://sso.garena.com/api/register',headers=headers,data=payload).json()
  if 'error' in str(reg):
    print('error')
  else:
    print(f'username:{name} - password:Fky@reg123 - email:{email}@gmail.com')
    file=open('accounts.txt','at')
    file.write(f'{name}|Fky@reg123|{email}@gmail.com\n')
    file.close()
for sl in range(0,int(input_sl)):
  reg_garena(input_name,input_email)
 
