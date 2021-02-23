class Router:
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interface = {}

    def add_int(self, int_name):
        self.interface[int_name] = ['-', 'not connect to any neighbor']

    def add_ip(self, int_name, ip):
        self.interface[int_name][0] = ip

    def add_connect(self, from_int, to_int, device):
        self.interface[from_int][1] = 'connect to device ' + \
            device.hostname + ' interface ' + to_int
        device.interface[to_int][1] = 'connect to device ' + \
            self.hostname + ' interface ' + from_int

    def change_hostname(self, new_name):
        self.hostname = new_name

    def show_int(self):
        print('Show interfaces of ' + self.hostname)
        print(self.hostname + ' has ' + str(len(self.interface)) + ' interfaces')
        for i in self.interface:
            print(i)

    def show_neighbor(self):
        for att in self.interface:
            print(att + ' ' + self.interface[att][1])
        print('\n')
