import pytest
from router import *
def test_change_hostname():
    r1 = Router('Cisco', 'IOSv', 'R1')
    r2 = Router('Cisco', '3745', 'R2')
    r3 = Router('Juniper', 'MXS', 'R3')

    r1.change_hostname('R1_NEW')
    r2.change_hostname('R2_NEW')
    r3.change_hostname('R3_NEW')

    assert r1.hostname == 'R1_NEW'
    assert r2.hostname == 'R2_NEW'
    assert r3.hostname == 'R3_NEW'

def test_add_int():
    r1 = Router('Cisco', 'IOSv', 'R1')
    r2 = Router('Cisco', '3745', 'R2')
    r3 = Router('Juniper', 'MXS', 'R3')

    r1.add_int('Serial 0/0')
    r2.add_int('Serial 0/3')
    r3.add_int('Serial 0/0')

    ans1 = {'Serial 0/0': ['-', 'not connect to any neighbor']}
    ans2 = {'Serial 0/3': ['-', 'not connect to any neighbor']}
    ans3 = {'Serial 0/0': ['-', 'not connect to any neighbor']}

    assert r1.interface == ans1
    assert r2.interface == ans2
    assert r3.interface == ans3


def test_add_ip():
    r1 = Router('Cisco', 'IOSv', 'R1')
    r2 = Router('Cisco', '3745', 'R2')
    r3 = Router('Juniper', 'MXS', 'R3')

    r1.add_int('Serial 0/1')
    r2.add_int('Serial 0/2')
    r3.add_int('Serial 0/2')

    r1.add_ip('Serial 0/1', '192.168.8.1')
    r2.add_ip('Serial 0/2', '192.168.9.1')
    r3.add_ip('Serial 0/2', '192.168.10.1')

    ans1 = {'Serial 0/1': ['192.168.8.1', 'not connect to any neighbor']}
    ans2 = {'Serial 0/2': ['192.168.9.1', 'not connect to any neighbor']}
    ans3 = {'Serial 0/2': ['192.168.10.1', 'not connect to any neighbor']}

    assert r1.interface == ans1
    assert r2.interface == ans2
    assert r3.interface == ans3



def test_add_connect():
    r1 = Router('Cisco', 'IOSv', 'R1')
    r2 = Router('Cisco', '3745', 'R2')
    r3 = Router('Juniper', 'MXS', 'R3')

    r1.add_int('Serial 0/1')
    r2.add_int('Serial 0/2')

    r1.add_ip('Serial 0/1', '192.168.8.1')
    r2.add_ip('Serial 0/2', '192.168.9.1')


    r1.add_connect('Serial 0/1', 'Serial 0/2', r2)

    ans1 = {'Serial 0/1': ['192.168.8.1', 'connect to device R2 interface Serial 0/2']}
    ans2 = {'Serial 0/2': ['192.168.9.1', 'connect to device R1 interface Serial 0/1']}
    
    assert r1.interface == ans1 and r2.interface == ans2
