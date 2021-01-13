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
    adult_tickets = 0 + int(input())
  except:
    ValueError
    print("Please Enter A Whole Number")

# Asking for Child Tickets
print("\n")
child_tickets = 0
while child_tickets == 0:
  try:
    print("Would you like any Child tickets?")
    print("Enter how many tickets you want in the section below:")
    child_tickets = 0 + int(input())
  except:
    ValueError
    print("Please Enter A Whole Number")

# Asking for Senior Tickets
print("\n")
Senior_tickets = 0
while Senior_tickets == 0:
  try:
    print("Would you like any Senior tickets?")
    print("Enter how many tickets you want in the section below:")
    Senior_tickets = 0 + int(input())
  except:
    ValueError
    print("Please Enter Whole A Number")

# Asking for Wristband Owners
print("\n")
Wristband_tickets = 0
while Wristband_tickets == 0:
  try:
    print("Would you like any Wristband tickets?")
    print("Enter how many tickets you want in the section below:")
    Wristband_tickets = 0 + int(input())
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
  answer = input("Enter yes or no:  ")
  print ("\n")
  if answer == "yes":
    Ticket_pass = 0 + 5
  elif answer == "no":
    Ticket_pass = 0
  elif ValueError:
    print ("You must enter  yes  or  no")


