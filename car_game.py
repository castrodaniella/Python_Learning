user_command = ""
started = False

while user_command.lower() != "quit":
    user_command = input("""What would you like to do: 
                         
    start - start car
    stop - stop a car
    quit - exit game: 
                         """).lower()
    if user_command == "start":
        if started:
            print("Car has already been started")
        else:
            started = True
            print("Car has been started")
    elif user_command == "stop":
        if not started:
            print("car has already been stopped")
        else:
            started = False
            print("Car has been stopped")
    elif user_command == "quit":
        print("Bye bye")
        break
    else:
        print("Invalid input please try again")