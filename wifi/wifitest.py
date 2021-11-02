import pywifi


def test_interfaces():
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()
    for interface in interfaces:
        print('interface: %s, status:%s'.format(interface.name(), interface.status()))


if __name__ == '__main__':
    test_interfaces()
