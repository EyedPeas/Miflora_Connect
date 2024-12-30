import configparser


def write_config():
    config = configparser.ConfigParser()

    config['devices'] = {"MacAddress": "5C:85:7E:13:2C:9E"}
    config['db'] = {"Database": "postgres", "Host": "localhost", "User": "marc", "Password": "fadewelt1993",
                    "Port": "5432"}

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

def get_database():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['db']['database']

def get_host():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['db']['host']

def get_user():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['db']['user']

def get_password():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['db']['password']

def get_port():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['db']['port']
