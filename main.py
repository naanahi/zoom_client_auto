import subprocess
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

meetingid = config_ini["DEFAULT"]["MEETINGID"]
password = config_ini["DEFAULT"]["PASSWORD"]

zoom_url = f"//zoom.us/join?action=join&confno={meetingid}&pwd={password}"
subprocess.run(f'start zoommtg:"{zoom_url}"', shell=True)