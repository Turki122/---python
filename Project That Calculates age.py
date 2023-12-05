#------
#------

# write A Very Beautiful Note
print("=" * 80)
print(" You can  Write The First Letter or Full Name of The Time Unit ".center(80,"="))
print("=" * 80)

#----collect Age Data

age = input("please write your Age :") .strip()

#--- collect Time unit Data

unit = input("Please Choose Time Unit : Months , weeks , Days ") .strip() .lower()

# get time Unit

months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == "months" or unit =="m":
    print("You Choosed The Unit months")
    print(f"you Lived for {months:,} months.")

elif unit =="weeks" or unit == "w":
    print("You Choosed The Unit Weeks")
    print(f"you Lived for {weeks:,} Weeks.")

elif unit =="days" or unit == "d":
    print("You Choosed The Unit Days")
    print(f"you Lived for {days:,} Days.")
