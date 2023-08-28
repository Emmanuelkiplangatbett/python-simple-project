command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Mnyama is already started buda!")
        else:
            started = True
            print("Mnyama started and ready to go")
    elif command == "stop":
        if not started:
            print("Mnyama is already stopped!")
        else:
            started = False
            print("Mnyama stopped to get some fuel.")
    elif command == "help":
        print("""
start - to start  mnyama
stop - to stop mnyama
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that")

