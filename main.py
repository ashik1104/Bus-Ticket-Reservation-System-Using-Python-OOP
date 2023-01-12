""" BUS TICKET RESERVATION SYSTEM """
""" CREATED BY : MD. ASHIK MAHMUD """
""" Email : ashikmahmud1104@gmail.com """


class user:
    def __init__(self, name, password):
        self.username = name
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_s, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_s = from_s
        self.to = to
        self.seat = ['Empty' for i in range(20)]


class Phitron_Company:  # For admin
    total_bus = 5
    bus_list = []

    def install(self):
        bus_no = int(input('Enter bus number : '))
        flag = False
        for bus in self.bus_list:  # checking whether any bus is already installed
            if bus_no == bus['coach']:
                print('Bus already installed')
                flag = True
                break
        if not flag:
            bus_driver = input('Enter the bus driver name : ')
            bus_arrival = input('Enter bus arrival time : ')
            bus_departure = input('Enter bus departure time : ')
            bus_from = input('Enter start place : ')
            bus_destination = input('Enter destination : ')
            new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_destination)
            self.bus_list.append(vars(new_bus))
            print('Bus installed successfully\n')


class Bus_counter(Phitron_Company):
    user_list = []

    def reservation(self):
        bus_seat = 20
        bus_no = int(input('Enter bus number : '))
        found = False
        for bus in self.bus_list:
            if bus['coach'] == bus_no:
                found = True
                passenger = input('Enter your name : ')
                seat_no = int(input('Enter your seat number : '))
                if seat_no - 1 > bus_seat:  # Maximum seat checking
                    print('Only 20 seats are available')
                    break
                elif bus['seat'][seat_no - 1] != 'Empty':  # Empty checking
                    print('Seat already booked')
                    break
                else:
                    bus['seat'][seat_no - 1] = passenger
                    break

        if not found:
            print('The bus is not installed')

    def show_bus_info(self):  # Info of a specific bus
        bus_no = int(input('Enter bus no : '))
        found = False
        for bus in self.bus_list:
            if bus['coach'] == bus_no:
                found = True
                print('*' * 50)
                print()
                print(f'{" " * 10} {"#" * 10} BUS INFO {"#" * 10}')
                print(f'Bus number : {bus_no} \t\t Driver : {bus["driver"]}')
                print(f'Arrival : {bus["arrival"]} \t\t\t Departure : {bus["departure"]}')
                print(f'From : {bus["from_s"]} \t\t To : {bus["to"]}')
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f'{a}. {bus["seat"][a - 1]}', end="\t")
                        a += 1
                    print('\t', end='\t')
                    for j in range(2):
                        print(f'{a}. {bus["seat"][a - 1]}', end="\t")
                        a += 1
                    print('\n')
                break
        if not found:
            print(f'Bus no {bus_no} is not available')

    def get_users(self):
        return Bus_counter.user_list

    def create_account(self):
        name = input('Enter your name : ')
        flag = 0
        for usr in Bus_counter.user_list:
            if usr['username'] == name:
                print('This username is not available')
                flag = 1
                break
        if flag == 0:
            password = input('Enter your password : ')
            new_user = user(name, password)
            Bus_counter.user_list.append(vars(new_user))
            print('Account created successfully')

    def available_buses(self):  # Information of all buses
        if len(self.bus_list) == 0:
            print('No bus available')
        else:
            for bus in self.bus_list:
                print('*' * 50)
                print()
                print(f'{" " * 10} {"#" * 10} BUS INFO {bus["coach"]} {"#" * 10}')
                print(f'Bus number : {bus["coach"]} \t\t Driver : {bus["driver"]}')
                print(f'Arrival : {bus["arrival"]} \t\t\t Departure : {bus["departure"]}')
                print(f'From : {bus["from_s"]} \t\t To : {bus["to"]}')
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f'{a}. {bus["seat"][a - 1]}', end="\t")
                        a += 1
                    print('\t', end='\t')
                    for j in range(2):
                        print(f'{a}. {bus["seat"][a - 1]}', end="\t")
                        a += 1
                    print('\n')


while True:
    counter = Bus_counter()
    print('1. Create an account.')
    print('2. Login to your account.')
    print('3. EXIT')
    user_input = int(input('Enter your choice : '))

    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        is_admin = False
        flag = 0
        if name == 'admin' and password == "123":
            is_admin = True
        if not is_admin:
            for usr in counter.get_users():
                if usr['username'] == name and usr['password'] == password:
                    flag = 1
                    break
            if flag == 1:
                while True:
                    print('1. available buses')
                    print('2. show bus info')
                    print('3. reservation')
                    print('4. EXIT')

                    usr_input = int(input('Enter your choice : '))
                    if usr_input == 1:
                        counter.available_buses()
                    elif usr_input == 2:
                        counter.show_bus_info()
                    elif usr_input == 3:
                        counter.reservation()
                    elif usr_input == 4:
                        break
            else:
                print('R a vai ke tomi????')
        else:
            while True:
                print('Hellow admin welcome back')
                print('1. Install bus')
                print('2. Available buses')
                print('3. show the info of a specific bus')
                print('4. show user list')
                print('5. EXIT')

                ur_input = int(input('Enter choice : '))
                if ur_input == 1:
                    counter.install()
                    print()
                elif ur_input == 2:
                    counter.available_buses()
                elif ur_input == 3:
                    counter.show_bus_info()
                elif ur_input == 4:
                    print(f'User list : {counter.get_users()}')
                    print()
                elif ur_input == 5:
                    print()
                    break
