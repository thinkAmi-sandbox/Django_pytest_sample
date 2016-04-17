import subprocess

def pytest_unconfigure(config):
    subprocess.run(['python', '-Wd', 'manage.py', 'check'], shell=True)