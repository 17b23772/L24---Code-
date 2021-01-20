from time import sleep
tickets = 0
while tickets != 500:
 # Listing Prices
  print("Welcome to Copington Adventure ThemePark")
  print("Ticket prices Adult- £20")
  print("Ticket prices Child(Below 14)- £12")
  print("Ticket prices Senior(60+) - £11")
  print("Wrist Band- £20")
  print("Parking Pass- Free")
  # Asking for Adult Tickets
  print("\n")
  adult_tickets = 0
  while adult_tickets == 0:
    try:
      print("Would you like any adult tickets?")
      print("Enter how many tickets you want in the section below:")
      print ("\n")
      adult_tickets = 0 + int(input())
    except:
      ValueError
      sleep(1)
      print ("\n")
      print("Please Enter A Whole Number")
      print ("\n")

  # Asking for Child Tickets
  print("\n")
  child_tickets = 0
  while child_tickets == 0:
    try:
      print("Would you like any Child tickets?")
      print("Enter how many tickets you want in the section below:")
      print ("\n")
      child_tickets = 0 + int(input())
    except:
      ValueError
      sleep(1)
      print ("\n")
      print("Please Enter A Whole Number")
      print ("\n")

  # Asking for Senior Tickets
  print("\n")
  Senior_tickets = 0
  while Senior_tickets == 0:
    try:
      print("Would you like any Senior tickets?")
      print("Enter how many tickets you want in the section below:")
      print ("\n")      
      Senior_tickets = 0 + int(input())
    except:
      ValueError
      sleep(1)
      print ("\n")
      print("Please Enter Whole A Number")
      print ("\n")
      

  # Asking for Wristband Owners
  print("\n")
  Wristband_tickets = 0
  while Wristband_tickets == 0:
    try:
      total_tickets = Senior_tickets + adult_tickets + child_tickets
      print("Would you like any Wristband tickets?")
      print("Wristband tickets allow you to go on the rides at Copington Adventure ThemePark.")
      print("\n")
      sleep(1)
      print (f"You currently have ordered {total_tickets} tickets in total. Each person only needs one wristband")
      sleep(1)
      print("Enter how many tickets you want in the section below:")
      Wristband_tickets = 0 + int(input())
      print ("\n")
    except:
      ValueError
      print("Please Enter A Whole Number")

  # Asking for the Lead Bookers 
  print("\n")

  print("Please enter the Lead Bookers Name (This is who will be billed)")
  print("Enter it in the space below")
  LeadB_tickets = input()


  #Asking if they want a ticket pass
  print("\n")

  Ticket_pass = 0
  while Ticket_pass == 0:
    print ("Do you want a Parking ticket? If you have been here before you can use your previous one. If not place it in the front of your car and it shows us that you have payed.")
    answer = input("Enter yes or no:  ").lower()
    print ("\n")
    if answer == "yes" :
      print ("Thanks! This will be printed at the end.")
      Ticket_pass = 0 + 5
    if answer ==  "y":
      print ("Thanks! This will be printed at the end.")
      Ticket_pass = 0 + 5
    elif answer == "no" "n":
      print("Please remember to place your ticket in your car window! ")
      Ticket_pass = 1
    elif answer == "n":
      print("Please remember to place your ticket in your car window! ")
      Ticket_pass = 1
    else:
      print ("You must enter  yes  or  no")

  #Creating the total cost. 
  print("\n")

  Total_cost = 0 
  while Total_cost == 0 : 
    Total_cost = adult_tickets * 20 + child_tickets * 12 + Senior_tickets * 11 + Wristband_tickets * 20 
    from time import sleep
    sleep(2)
    print (f"Your total cost is: £{Total_cost}") 
  
  print("\n")
  # Figuring out their prices. 
  from time import sleep
  sleep(2)
  print("\n")
  print ("Would you like to pay in £10 or £20 notes?")
  print("\n")
  print ("To pay in £20 enter large , To pay in £10 enter small .")
  large = 20
  small = 10
  twe_notes = Total_cost // 20
  ten_notes = Total_cost // 10
  choice = str(input()).lower()

  large_choice = 0
  small_choice = 0

  while large_choice == 0:
    if choice == "large":
      print("\n")
      print("You are paying in £20")
      from time import sleep
      sleep(2)
      print("\n")
      twe_notes = Total_cost // 20 
      print (f"That will be {twe_notes} twenty pound notes.")
      money = 0
      while money != twe_notes:
        print (f"You are paying {twe_notes} twenty pound notes in total.")
        print(f"Enter {twe_notes} twenty pound notes. (Enter the number requested)")
        money = money + int(input())
        print ("\n")
        print (f"You have paid for {money} twenty pound notes.")
        large_choice = large_choice + 2
    else:
      print("Please enter Large or Small")
      print ("\n")
  print ("Do you want change. Enter Yes or No")
  answer = str(input()).lower()
  if answer == "yes" "y":
    print ("\n")
    total = ten_notes * small 
    change = Total_cost - total
    print (f"You have £{change} of change. ")
    sleep(2)
    print ("Please recieve change from the coin slot below.")
    from time import sleep
    sleep(3)
    print ("\n")
    print ("\n")
  elif answer == "no" "n":
    print ("\n")
    print ("Thank You!")
    print ("\n")
  total_tickets = adult_tickets + Senior_tickets + child_tickets
  print ("Here is your ticket!")
  print (f"Ticket under name {LeadB_tickets} ")
  print (f"Tickets Purchased {total_tickets}")
  from datetime import date
  today = date.today()
  print("Today's date:", today)

  while small_choice == 0:
    if choice == "small":
      sleep(2)
      print("\n")
      print("You are paying in £10")
      print("\n")
      ten_notes = Total_cost // 10
      print (f"That will be {ten_notes} ten pound notes.")
      money = 0
      while money != ten_notes:
        print (f"You are paying {ten_notes} ten pound notes in total.")
        print(f"Enter {ten_notes} ten pound notes")

        money = money + int(input())
        print ("\n")
        print (f"You have paid for {money} ten pound notes.")
        print("\n")
      print ("\n")
    print ("Do you want change?")
    answer = str(input()).lower()
    if answer == "yes":
      print ("\n")
      total = ten_notes * small 
      change = Total_cost - total
      print (f"You have £{change} of change. ")
      sleep(2)
      print ("Please recieve change from the coin slot below.")
      from time import sleep
      sleep(3)
      print ("\n")
      print ("\n")
    elif answer == "no":
      print ("\n")
      print ("Thank You!")
      print ("\n")
      sleep(3)
    total_tickets = adult_tickets + Senior_tickets + child_tickets
    print ("Here is your ticket!")
    print (f"Ticket under name {LeadB_tickets} ")
    print (f"Tickets Purchased {total_tickets}.")
    from datetime import date

    today = date.today()
    print("Today's date:", today)

    print("\n")
    print("Thanks for Buying Your Tickets.")

  if Ticket_pass == 5:
    sleep(2)
    print("\n")
    print ("Here is your Ticket Pass")
    print ("Put this at the window of your car.")
  else:
    print("\n")
    print ("Remeber to put your ticket pass in the front of your car.")
    print("\n")
    print("\n")
  print("\n")
  sleep(2)
  tickets = tickets + 1
  total_tickets = 500 - tickets
  print (f"There are {total_tickets} tickets left.")
  if total_tickets == 0:
    print ("We are out of Tickets! Sorry")
    break
  print("\n")
  print("\n")
  print("\n")
  
  print ("Next Customer Please")
  print("\n")
  print("\n")
  print("\n")