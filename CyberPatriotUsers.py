import subprocess
def add_user(uname):
    subprocess.call(["sudo","useradd","-m",uname])
    p = subprocess.Popen(["sudo","passwd",uname])
def del_user(uname):
    subprocess.call(["sudo","userdel","-r",uname])
def add_admin(uname):
    subprocess.call(["sudo","usermod","-a","-G","sudo",uname])
def del_admin(uname):
    subprocess.call(["sudo","userdel",uname,"sudo"])
default_users = ['root', 'daemon', 'bin', 'sys', 'sync', 'games', 'man', 'lp', 'mail', 'news', 'uucp', 'proxy', 'www-data', 'backup', 'list', 'irc', 'gnats', 'nobody', 'libuuid', 'syslog', 'messagebus', 'usbmux', 'dnsmasq', 'avahi-autoipd', 'kernoops', 'rtkit', 'saned', 'whoopsie', 'speech-dispatcher', 'avahi', 'lightdm', 'colord', 'hplip', 'pulse']

requested_users = set(input("users: ").split(",")+default_users)#this is bc of weirdness with shell and newlines, otherwise it would make sense to split by newline
requested_admins = set(input("admins: ").split(","))

current_user_list = subprocess.check_output(['getent', 'passwd']).decode().split("\n")
print(current_user_list)
current_user_list = [x.split(":")[0] for x in current_user_list]
print(current_user_list)
current_admin_list = subprocess.check_output(['getent', 'group', 'sudo']).decode().split("\n")
print(current_admin_list)
current_admin_list = [x.split(":")[3] for x in current_admin_list[:-1]]
print(current_admin_list)

users_to_add = requested_users.difference(current_user_list)
print(users_to_add)
input()
for user in users_to_add:
    add_user(user)
    
users_to_remove = current_user_list.difference(requested_users)
print(users_to_remove)
input()
for user in users_to_remove:
    del_user(user)
    
admins_to_add = requested_admins.difference(current_admin_list)
print(admins_to_add)
input()
for admin in admins_to_add:
    add_admin(admin)

admins_to_remove = current_admin_list.difference(requested_admins)
print(admins_to_remove)
input()
for admin in admins_to_remove:
    remove_admin(admin)
