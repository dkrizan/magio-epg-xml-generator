import datetime
import getopt
import sys
from getpass import getpass
from src.service import MagioGo, UserNotDefinedException, UserInvalidException

username: str = ""
password: str = ""
days = 7


def valid_login():
    return len(username) or len(password)


def usage():
    print("python" + __file__ + "\n")
    print("Arguments:")
    print("\t-d, --days <days>\tNumber of days of epg to generate")
    print("\t-u, --username <USERNAME>")
    print("\t-p, --password <PASSWORD>")


def error(message: str):
    print("Error: " + message)
    sys.exit(2)


try:
    opts, args = getopt.getopt(sys.argv[1:], "hu:p:d:", ["days", "username", "password"])
except getopt.GetoptError:
    usage()
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        usage()
        sys.exit(2)
    elif opt in ("-u", "--username"):
        username = arg
    elif opt in ("-p", "--password"):
        password = arg
    elif opt in ("-d", "--days"):
        days = int(arg)

if not (len(username) or len(password)):
    username = input("Username: ")
    password = getpass("Password: ", sys.stderr)
service = MagioGo(username, password)
from_date = datetime.datetime.now()
try:
    channels = service.channels()
    epg = service.epg(channels, from_date, days)
    service.export_epg('epg.xml', channels, epg)
except UserNotDefinedException:
    error('Username or password not entered')
except UserInvalidException:
    error('Invalid credentials')
