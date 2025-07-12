import os
import scratchattach as sa

# Empty
# ------------------------------------------------------
# ------------------------------------------------------

# Functions
# ------------------------------------------------------
def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def whatshappening(feednumber):
    activity = session.feed(limit=1, offset=feednumber).__getitem__(0)

    if activity.type == "loveproject":
        print("| " + activity.actor_username + " loved the project " + activity.title + " (" + str(activity.project_id) + ")")
    elif activity.type == "addcomment":
        print("| " + activity.actor_username + " commented '" + activity.comment_fragment + "'")
    elif activity.type == "followstudio":
        print("| " + activity.actor_username + " followed the studio " + activity.title + " (" + str(activity.gallery_id) + ")")
    elif activity.type == "favoriteproject":
        print("| " + activity.actor_username + " favorited the project " + activity.project_title + " (" + str(activity.project_id) + ")")

def messages(messagenumber):
    messages = session.messages(limit=1, offset=messagenumber).__getitem__(0)

    if messages.type == "curatorinvite":
        print("| " + messages.actor_username + " invited you to " + messages.title + "(" + str(messages.gallery_id) + ")")
    elif messages.type == "followuser":
        print("| " + messages.actor_username + " is now following you!")
    elif messages.type == "favoriteproject":
        print("| " + messages.actor_username + " favorited your project " + messages.project_title + "(" + str(messages.project_id) + ")")
    elif messages.type == "loveproject":
        print("| " + messages.actor_username + " loved/hearted your project " + messages.title + "(" + str(messages.project_id) + ")")
    elif messages.type == "remixproject":
        print("| " + messages.actor_username + " remixed your project " + messages.parent_title + "(" + str(messages.parent_id)+ "), their level is " + messages.title + "(" + messages.project_id + ")")
    elif messages.type == "addcomment":
        print("| " + messages.actor_username + " commented '" + messages.comment_fragment + "' on your project.")


# ------------------------------------------------------

# Login
# ------------------------------------------------------
print("Login Form")
print("If you do not have a scratch account, sign up at scratch.mit.edu/join")
print("")

usrnm = str(input("Username: "))
passwrd = str(input("Password: "))

session = sa.login(usrnm, passwrd)

clear()
# ------------------------------------------------------

# Main Page
# ------------------------------------------------------
if session.banned == True:
    print("The scratch account " + session.username + " is banned, you cannot access Scratch.py, if you do wish to access Scratch.py, please use a different account.")
    exit()

print("Logged in as " + session.username + ".")
print("")

print("Welcome to Scratch.py, a fully functional scratch browser made in python.")
print("")

print("What's Happening?")
whatshappening(0)
whatshappening(1)
whatshappening(2)
whatshappening(3)
whatshappening(4)

print("")
print("What will be your next destination? (Exit, Messages)")
nextdest = str(input("Destination: "))
# ------------------------------------------------------

# Messages
# ------------------------------------------------------
if nextdest == "Messages":
    msgamount = int(input("How many messages would you like to see?: "))

    for i in range(msgamount):
        messages(i)

    markasread = str(input("Would you like to mark ALL of your messages as read? (y/n): "))

    if markasread == "y":
        session.clear_messages()

    exit()
# ------------------------------------------------------

# Exit
# ------------------------------------------------------
elif nextdest == "Exit":
    exit()
# ------------------------------------------------------
