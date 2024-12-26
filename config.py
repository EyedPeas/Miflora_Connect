import configparser


def write_config():
    config = configparser.ConfigParser()

    config['devices'] = {"MacAddress": "5C:85:7E:13:2C:9E"}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print(config.sections())

def get_mac_address():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['devices']['MacAddress']
