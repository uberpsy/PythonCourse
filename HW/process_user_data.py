import csv

def read_user_data():
    user_data = []
    with open('user_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_data.append(row)
    return user_data

def print_all_users(user_data):
    print("\nAll users:")
    for user in user_data:
        print_user_info(user)

def print_average_age(user_data):
    ages = [int(user['age']) for user in user_data]
    average_age = sum(ages) / len(ages)
    print(f"\nAverage age: {average_age}")

def find_users_by_city(user_data):
    cities = set(user['city'] for user in user_data)
    print("\nCities:", list(cities))
    city = input("Enter city: ")
    print(f"Users from {city}:")
    for user in user_data:
        if user['city'] == city:
            print_user_info(user)

def print_user_info(user):
    print(f"\tUser name: {user['name']}")
    print(f"\tUser age: {user['age']}")
    print(f"\tUser city: {user['city']}\n")

def sort_users_by_name(user_data):
    sorted_users = sorted(user_data, key=lambda x: x['name'])
    print("\nUsers sorted by name:")
    for user in sorted_users:
        print_user_info(user)

def main():
    user_data = read_user_data()

    while True:
        print("\n1. Print all users")
        print("2. Print average users age")
        print("3. Find users by city")
        print("4. Sort users by name")
        print("5. Quit")
        print("****************************")
        choice = input("Enter your choice: ")

        if choice == '1':
            print_all_users(user_data)
        elif choice == '2':
            print_average_age(user_data)
        elif choice == '3':
            find_users_by_city(user_data)
        elif choice == '4':
            sort_users_by_name(user_data)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()