import time
import replit
global year

def Options():
	global Opinion
	print("This code contains the NRIC Validation Algorithm.")
	Opinion = input("Include NRIC Validation Algorithm?(Y/N) : ")
	if Opinion == "Y" or Opinion == "y":
		RunAll()
	elif Opinion == "N" or "n":
		RunLess()
	else:
		print("Invalid Input!")
		time.sleep(2.5)
		replit.clear()
		Options()
		
def Rerun():
	Confirm = str(input("\nRerun the code?[Y or N] : "))
	if Confirm.startswith('Y') or Confirm.startswith('y'):
		if Opinion == "Y" or "y":
			replit.clear()
			RunAll()
		elif Opinion == "N" or "n":
			replit.clear()
			RunLess()	
	elif Confirm.startswith('N') or Confirm.startswith('n'):
		replit.clear()
		exit()
	else:
		print("Invalid Input!")
		time.sleep(1.5)
		Options()


def CheckNRIC():
	global NRIC
	replit.clear()
	NRIC = str(input("Input NRIC here: "))
	NRIC = NRIC.upper()
	if len(NRIC) != 9:
		print("Invalid NRIC Number!")
		time.sleep(2.5)
		replit.clear()
		CheckNRIC()
	elif NRIC[-1].isdigit() or NRIC[0].isdigit():
		print("Invalid NRIC Number!")
		time.sleep(2.5)
		replit.clear()
		CheckNRIC()
	elif not NRIC[1:8].isdigit():
		print("Invalid NRIC Number!E")
		time.sleep(2.5)
		replit.clear()
		CheckNRIC()
   

def CheckValid():
  y = 0
  a = 0
  b = 1
  x = 0
  ST = ['J','Z','I','H','G','F','E','D','C','B','A']
  FG = ['X','W','U','T','R','Q','P','N','M','L','K']

  
  NRICint = NRIC[1:-1]
  NRICweight = "2765432"
  while x != 7:
    y = y + (int(NRICweight[a:b])) * (int(NRICint[a:b]))
    a += 1
    b += 1
    x += 1
  if NRIC.startswith('S') or NRIC.startswith('F'):
    y = y % 11
  
  elif NRIC.startswith('T') or NRIC.startswith('G'):
    y += 4
    y = y % 11
  
  if NRIC.startswith('S') or NRIC.startswith('T'):
    if ST[y] == NRIC[-1]:
      print("This NRIC is a Valid NRIC")
    else:
      print("This NRIC is a Invalid NRIC!")
      time.sleep(2.5)
      replit.clear()
      Rerun()
  elif NRIC.startswith('F') or NRIC.startswith('G'):
    if FG[y] == NRIC[-1]:
      print("This NRIC is a Valid NRIC")
    else:
      print("This NRIC is a Invalid NRIC!")
      time.sleep(2.5)
      replit.clear()
      Rerun()
  else:
    print("Invalid NRIC!")
    time.sleep(2.5)
    replit.clear()
    Rerun()



def CheckNational():
  global year
  global Nationality
  if NRIC.startswith('S'):
    year = 1900
    Nationality = "Singapore Citizen or Singapore PR"
  elif NRIC.startswith('T'):
    year = 2000
    Nationality = "Singapore Citizen or Singapore PR"
  elif NRIC.startswith('F'):
    year = 1900
    Nationality = "Foreigner"
  elif NRIC.startswith('G'):
    year = 2000
    Nationality = "Foreigner"
  else:
    print("Invalid NRIC")
    time.sleep(2.5)
    replit.clear()
    Rerun()


def Output():
	global year
	if (int(NRIC[1:3])) < 68 and (NRIC.startswith('S') or NRIC.startswith('F')):
		replit.clear()
		print("\nYour age is more than 52")
	else:
		year = int(NRIC[1:3]) + year
		age = 2020 - year
		replit.clear()
		print('Your age is ' + str(age))
	print("\nNationality: " + Nationality)


def RunAll():
	CheckNRIC()
	CheckNational()
	CheckValid()
	Output()
	Rerun()

def RunLess():
	CheckNRIC()
	CheckNational()
	Output()
	Rerun()

Options()
