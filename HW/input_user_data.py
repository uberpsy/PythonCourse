import csv

def data_input():
    user_data = []
    while True:
        new_data = input("\nEnter new user data [y/n]?: ")
        if new_data.lower() != 'y':
            break
        name = input("Enter user name: ")
        age = int(input("Enter user age: "))
        while True:
            if age <= 0 :
                print('Age must be positive and bigger than zero number)')
                age = int(input("Enter user age: "))
            else:
                break
        city = input("Enter user city: ")
        user_data.append({'name': name, 'age': age, 'city': city})

    save_to_csv(user_data)
    print("\nUser data saved to 'user_data.csv'.")

def save_to_csv(user_data):
    with open('user_data.csv', mode='w', newline='') as file:
        fieldnames = ['name', 'age', 'city']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for user in user_data:
            writer.writerow(user)

if __name__ == "__main__":
    data_input()