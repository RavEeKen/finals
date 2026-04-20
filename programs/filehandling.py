try:
    first_note = input("Enter your first short note/message: ")
    with open("notes.txt", "w") as file:
        file.write(first_note + "\n")
    print("First note saved to notes.txt successfully!")

    print("\n--- Content of notes.txt ---")
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)
    print("-----------------------------")

    second_note = input("\nEnter another note to append: ")
    with open("notes.txt", "a") as file:
        file.write(second_note + "\n")
    print("Second note appended successfully!")

    print("\n--- Updated content of notes.txt ---")
    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print(updated_content)
    print("------------------------------------")

except FileNotFoundError:
    print("Error: File 'notes.txt' not found. Please check if the file exists.")
except PermissionError:
    print("Error: Permission denied. Check file permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
