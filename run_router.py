from router import *

r1 = Router('Cisco', 'IOSv', 'R1')
r2 = Router('Cisco', '3745', 'R2')
r3 = Router('Juniper', 'MXS', 'R3')

r1.add_int('Serial 0/1')
r1.add_int('Serial 0/2')
r2.add_int('Serial 0/1')
r2.add_int('Serial 0/2')
r2.add_int('Serial 0/3')
r3.add_int('Serial 0/1')
r3.add_int('Serial 0/2')

r1.add_ip('Serial 0/1', '192.168.1.1')
r1.add_ip('Serial 0/2', '192.168.2.1')
r2.add_ip('Serial 0/1', '192.168.3.1')
r2.add_ip('Serial 0/2', '192.168.4.1')
r2.add_ip('Serial 0/3', '192.168.5.1')
r3.add_ip('Serial 0/1', '192.168.6.1')
r3.add_ip('Serial 0/2', '192.168.7.1')

r1.add_connect('Serial 0/1', 'Serial 0/2', r2)
r1.add_connect('Serial 0/2', 'Serial 0/1', r3)
r2.add_connect('Serial 0/1', 'Serial 0/2', r3)

r1.change_hostname('R1-NEW')
r2.change_hostname('R2-NEW')
r3.change_hostname('R3-NEW')


r1.show_int()
r1.show_neighbor()

r2.show_int()
r2.show_neighbor()


r3.show_int()
r3.show_neighbor()
