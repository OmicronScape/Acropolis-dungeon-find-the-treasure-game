print('''

        __..--.                                   _.._
    _..--''_______|-._____  ______________________|``  __``--.._
   '-.-..---..---..---..--''.---..---..---..---..---..---..---.-'
     |_::___::___::___::___::___::___::___::___::___::___::___|
     |________________________________________________________|
     '.--.':'.--.' '.--.'  '.--.'  '.--.'  '.--.' '.--.' '.--.'
      |''|.|.|''|-. |''|    |''|    |''|    |''|   |''|.|.|''|
      |''|.| |''| | |''|    |''|    |''|    |''|   |''| |.|''|
      |''|.|.|''| | |''|    |''|    |''|    |''| _,|''|.|.|''|
      |''|.| |''|.| |''|    |''|    |''|    |''|/ .|''| |.|''|
      |''|.|.|''| |_|''|`.__|''|,--'|''|``-.|''|   |''|.|.|''|
      |''|.| |''| |.|''| |  |''|  __|''|   ||''|.  |''| |.|''|
      |''|.|.|''| | |''| |  |''| |  |''|   ||''|   |''|.|.|''|
      |''|.| |''|.| |''| |  |''| |  |''|   ||''|  .|''| |.|''|
      |''|.|.|''| | |''| |__|''|_|__|''|___||''|   |''|.|.|''|
      |''|_|_|__| |.|''|'   |''|    |''|    |''|-._|''| |.|''|
      |'/  )| | ||  |''|    |''|    |''|    |''|   |''|'|.|''|
    .-'|`-' | | ||--''''----''''----''''----''''---''''---''''-.
  .'---|| | | |,''--.,-------------------.----------------------'.
 '-----|| | | /  - - - - - - - - ,---. -  \-----------------------'
       || | | : _ _,---._ _ _ _ _`._.'_ _ :                     SSt
       ||_|_|_\  _ `---' _ _ _ ,._ _ _ _  /
               `--------------'--`-------'
''')
print("Welcome the Acropolis dungeon!")
print("You are a burglar in ancient Greece and you heard rumors that there is hidden treasure room beneath Acropolis.")
print("Your mission is to wait until nightfall and enter Acropolis to find that treasure.")
print("You managed to pass the entrance guards silently and went down the stairs inside the dungeon....")
path1 = input('As you follow the dark corridor you see two pathways.Which way you wonna go?Type "left" or "right". :  \n').lower()
if path1 == "left":
    print("You continue walking the path and you end up in a large sewer with dirty water in the middle.")
    print("Across you see a wooden door and in front of you there is also a lever.")
    print("You here noices behind you....it must be the Guard patrol!!!")
    path2 = input('what are you going to do?Walk through the filthy waters OR use the lever?Type "water" or "lever". : \n').lower()
    if path2 == "water":
        print("You managed to pass through the waters with success,you opened the door and entered the room!")
        print("A large chest lies in the middle of the room and you can clearly see that it is locked.")
        print("What is your next move?you try to unlock it with your skills or search the room for something to unlock it?")
        path3 = input("Type unlock or search: \n").lower()
        if path3 == "unlock":
            print("As a skilled burglar you managed to unlock it...the chest is full of gold coins!!!\nThe treasure is all yours!!!")
        elif path3 == "Search":
            print("You searched everything in the room and you found nothing that could help you open the chest.")
            print("You wasted to much time searching and you are cought by the guards!!The punishment of thievery is death!\nGame Over!!")
    elif path2 == "lever":
        print("You pulled the lever and a wooden bridge starts to fall so you can walk across but it was very noisy.")
        print("Guards heard the noise and start running to your location.\nGame over!!! ")


elif path1 == "right":
    print("This path leads to a lethal arrow trap.You are dead!\nGame over!!")