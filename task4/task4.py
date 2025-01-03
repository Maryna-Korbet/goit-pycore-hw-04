def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: dict):
  name, phone = args
  existing_phone = contacts.get(name)
  if not existing_phone:
    return f"contact with name {name} does not exist"
  
  contacts[name] = phone
  return "Contact updated."

def show_phone(args, contacts: dict):
  [name] = args
  existing_phone = contacts.get(name)
  if not existing_phone:
    return f"contact with name {name} does not exist"
  
  return existing_phone

def show_all(contacts: dict):
  if not contacts.keys():
    return "There is no contacts in the list"
  
  result = []
  for name, phone in contacts.items():
    result.append(f"{name} {phone}")
  return "\n".join(result)


def main():
    print("Welcome to the assistant bot!")
    print("Type 'hello' to start or 'exit' to quit.")
    contacts = {}

    while True:
        user_input = input("Enter command: ").strip()
        if not user_input:
            continue  
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")
      
if __name__ == '__main__':
  main()

