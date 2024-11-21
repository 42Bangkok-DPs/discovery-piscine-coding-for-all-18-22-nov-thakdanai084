while True:
    user_input = input("Please enter something (or type 'STOP' to exit): ")

    if user_input.upper() == "STOP":
        print("Exiting the program. Goodbye!")
        break
    else:
        print(f"I got that: {user_input}")
