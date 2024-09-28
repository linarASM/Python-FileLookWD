import os

def list_files():
    for file in os.listdir('.'):
        print(file)

def change_directory(path):
    try:
        os.chdir(path)
        print(f"USdir: {os.getcwd()}")
    except FileNotFoundError:
        print("Dir error.")

def display_help():
    print("Commands:")
    print("ls")
    print("cd")
    print("help")
    print("exit")

def main():
    while True:
        command = input("X: ").strip()
        if command == "ls":
            list_files()
        elif command.startswith("cd "):
            path = command[3:].strip()
            change_directory(path)
        elif command == "help":
            display_help()
        elif command == "exit":
            print("Exit...")
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()
