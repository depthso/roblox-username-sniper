names =  10 # Amount of usernames to save
length =  5 # Length of usernames
file = 'valid.txt' # Automatically creates file

#------------#

import requests, random, string, time

Found = 0

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	GRAY = '\033[90m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def Success(Username):
	print(f"{bcolors.OKBLUE}[{Found}/{names}] [+] Found Username: {Username} {bcolors.ENDC}")

	with open(file, 'a+') as f:
		f.write(f"{Username}\n")

def Taken(Username):
	print(f'{bcolors.FAIL}[-] {user} {bcolors.ENDC}')

def MakeUsername(length):
   letters = string.ascii_lowercase + string.digits
   return ''.join(random.choice(letters) for i in range(length))

def CheckUsername(Username):
	Birthday = '1999-04-20'
	Url = f'https://auth.roblox.com/v1/usernames/validate?request.username={Username}&request.birthday={Birthday}'
	
	Data = requests.get(Url)
	Json = Data.json()

	Code = Json['code']
	return Code

# Check usernames loop
while Found < names:
	try:
		Username = MakeUsername(length)
		Code = CheckUsername(Username)
		
		if Code == 0:
			Found += 1
			Success(Username)
		else:
			Taken(Username)
				
	except Exception as e:
		print('Error:', e)

	time.sleep(50/1000)

print(f"{bcolors.OKBLUE}[!] Finished {bcolors.ENDC}")
