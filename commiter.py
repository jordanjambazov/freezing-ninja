import os
import subprocess

from faker import Faker

DIR = os.path.dirname(__file__)
DUMMY_FILE = 'test.txt'

def main():
    #os.chdir(DIR)
    dummy_file = open(DUMMY_FILE, 'a')
    load = os.getloadavg()
    fake = Faker()
    message = fake.text(50)
    dummy_file.write(str(load) + "\n")
    dummy_file.close()
    subprocess.call(["git", "add", DUMMY_FILE])
    subprocess.call(["git", "commit", "-m", '"{}"'.format(message)])
    subprocess.call(["git", "push", "origin", "master"])



if __name__ == '__main__':
    main()
