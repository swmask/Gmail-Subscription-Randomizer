Username = input("Enter Email: ")
at_sign = "@"
User = ""
Subscription = "+" + input("Subscription Name: ") + '@gmail.com'
is_email = False

for letter in Username:
    if letter == at_sign:
        is_email = True
        break
    User += letter
    
User += Subscription
print(User)

## Option 2 - (Find where the @ is and use it's location to determine what to keep from the string)
#for i in range(len(Username)):
#    if Username[i] == at_sign:
#        is_email = True
#        break
#if is_email == True:
#    User = Username[0:i]
#    Username = User + Subscription
#    print(Username)

## Option 3 - (Use the split function)
#if is_email == True:
  #  Username = Username.split('@')[0] + Subscription
  #  print(Username)

## Option 4 - (Use partition function)
#if is_email == True:
  #  Username = Username.partition(at_sign)[0] + Subscription
  #  print(Username)
#else:
#    Username += Subscription
#    print(Username)