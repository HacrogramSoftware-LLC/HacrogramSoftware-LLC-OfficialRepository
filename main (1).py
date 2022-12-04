import time
import random
import warnings
import os

#=================010
Bankbal=100
debt=0
shift=False
user=input("Input a username!> ")
print("BE CAREFUL! Gambiling is highly addictive and can cause mental health issues.")
print("""Also dont go broke 
- -
<-> """)
lottowheel = [1000000,10000,1000,800,800,600,600,600,600,400,400,400,400,400,400,200,200,200,200,200,200,200,200,200,200,200,200,200,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,1,100,100,100,100,100,100,100,100,100,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,200,200,200,200,200,200,200,200,200,200,200,200,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
#==main defs======

def main():
  global heistnumW
  heistnumW = [1]
class OwnedCars():
  class fordFiesta():
    year="2019"
    brand="Ford"
    model="Fiesta"
    price=9500
    fuel="DIESEL"
    owned=False
    Owner=""
    ownerstr="False"
    
  class fiat500():
    year="2017"
    brand="Fiat"
    model="500"
    price=7750
    fuel="DIESEL"
    owned=False
    Owner=""
    ownerstr="False"
  class hummerH1():
    year="2003"
    brand="Humvee"
    model="H1"
    fuel="petral"
    owned=True
    Owner="John Doe"
    ownerstr="True"
class OwnedHouses():
  class Mry133():
    adress="133 Mrytle Way"
    owned=False
    ownedstr="False"
    Owner=""

carOpt=""
carConf=""
chosenCar=""
chosenPrice=""

def heist():
    global Bankbal
    global heistnumW
    if Bankbal<=20:
      print("insufficent funds")
      options()
    if Bankbal>=20:
  	  print("starting")
  	  giggles=random.choice(heistnumW)
  	  heistnum1=input("input a number> ")
  	  if heistnum1 == giggles:
  	  	print("you won 150 tokens")
  	  	Bankbal+=150
  	  	print("heist successful")

  




def carDealer():
  global Bankbal
  global carOpt
  global carConf
  global chosenCar
  global chosenPrice
  
  print("Welcome to the Atkins Car Dealer!")
  print("=== | Car Market | ===")
  print("= 01- 2019 Ford Fiesta - £9,500 =")
  print("= 02- 2017 Fiat 500 - £7,750 =")
  print("= 03- Return to menu - =")
  carOpt=("Select an option: ")
  if carOpt=="01":
    chosenCar="2019Fiesta"
    chosenPrice=OwnedCars.fordFiesta.price
    print("Are you sure you want to purchase: 2019 Ford Fiesta?")
    carConf == input("Y/N: ")
    if carConf == "Y" or carConf == "y":
      Bankbal - chosenPrice
      print("Congratulations! You now own a 2019 Ford Fiesta!")
    if carConf == "N" or carConf == "n":
      carDealer()
    


def ownedhouses():
  print((OwnedHouses.Mry133.adress,(OwnedHouses.Mry133.ownedstr),OwnedHouses.Mry133.Owner))
def home():
	global Bankbal
	print(" welcome to the market!")
	print("=======house market=======")
	print("=01- 133 Mrytle Way £10k =")
	print("==========================")
	opt6= input("select a property to buy> ")
	if opt6=="01":
		if Bankbal>=10000:
			Bankbal -=10000
			print("you own 133 Myrtle way ")
      
  
			options()
		if Bankbal<=10000:
			print("Insufficient Funds You have ",Bankbal,"Tokens" """
   
     
     
     and you're a brokie """)#for a little fun -R3tr0
			options()

def market():
	print("====Hello Welcome to the market====")
	print("= Aspa-01                         =")
	print("= house market-02                 =")
	print("= car market-03                   =")

	opt5=input("input an option-")
	if opt5 =="02":
		home()
	if opt5 =="03":
		carDealer()
def lotto():
	global Bankbal
	print("by entering the gamble feature you have spent 100 tokens")
	if Bankbal>=100:
		Bankbal -= 100
		win=random.choice(lottowheel)
		print("You won ", win, "!")
		print("Congratulations!")
		Bankbal += win
		options()
	else:
		print("Insurficiant funds!")
		options()

	

		

def custom():
  global Bankbal
  print("=============")
  print("=01 restart =")
  print("=============")
  opt7=input("please input an option>")
  if opt7=="01":
	  Bankbal=100
	  options()
		
def bank():
	print("|===Bank options===|")
	print("| 01- check balance|")
	print("| 02- deposit      |")
	print("| 03- withdraw     |")
	print("|==================|")
	opt3 = input("Input a valid ID[0X]")
	if opt3 =="01":
		print("==Balence==")
		print("= balence- ",Bankbal,"=")
		options()
def work():
  print("|===Choose A WorkPlace========|")
  print("| 01-Lementom Lab[5toks/3mins]|")
  print("| 02-McRonalds[1toks/10mins]  |")
  print("| 03-CFK[1toks/1mins]         |")
  print("|=============================|")
  opt4=input("Choose a job by id [0X]> ")
  if opt4 =="01":
    global Bankbal
    print("welcome to Lementom labs ")
    print("you are on shift for 5 mins")
    time.sleep(3)
    shift=True
    print("please be patient")
    workfor=int(input("Enter max pay Cap> "))
    

    while shift==True:
      if workfor>=1000:
        print("Invalid Amount! [max:10k]")
        break
      
      time.sleep(10)
      Bankbal+=5
      print("Youve been payed! you have ",Bankbal,"Tokens!")
      if Bankbal>=workfor:
          print("Work Max Cap Reached")
          options()
          break
  if opt4 =="03":
	  global Bankal
	  print("welcome to CFK")
	  print("your on shift for 1 mins")
	  time.sleep(1)
	  Bankbal+=1
	  print("Thanks for the help")
	  options()
  if opt4 =="02":
	  print("welcome to McRonalds")
	  print("you are on shift for 10 mins")
	  time.sleep(2)
	  Bankbal+=1
	  options()


def mainfunc():
  print("===Hello Welcome to GMBLR.net/replit===")
  options()

def options():

	print("|=====MENU======|")
	print("║01- gamble     ║")
	print("║02- work       ║")
	print("║03- bank       ║")
	print("║04- options    ║") 
	print("║05- Market     ║")
	print("║06-Owned houses║")
	print("║07- heists     ║")
	print("================║")
	opt1=input("please input a number to continue[0X]") 
	if opt1 =="01":
		lotto()
	if opt1 =="03":
		bank()
	if opt1=="02":#leaving my mark from kyle ;)
		work()
	if opt1 =="05":#Nathan was here ;)))))
		market()
	if opt1 =="04":
		custom()
	if opt1=="06":
		ownedhouses()
	if opt1=="07":
		heist()
	if opt1 != "01"or"02"or"03"or"04"or"05"or"06"or"07":
		options()
		#===end MDefs=====
mainfunc()

#Numbers Deleted For privacy Reason
