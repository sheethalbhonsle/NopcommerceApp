import configparser
#configparser is a package , inside it there is a class called RawConfigParser, i have created object called config
#this object(config) has methods which can be used to read ini files
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

#how to get data from ini, thts we need to create class
#this is not pytest, its python class
#static methods can be directly accessed using class name, no need to create objects
#for every variable we need to create method
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password= config.get('common info', 'password')
        return password
