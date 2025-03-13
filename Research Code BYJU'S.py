import subprocess packages = ['requests', 'beautifulsoup4', 'urllib3', 'html5lib']

for package in packages:
    subprocess.run(['pip', 'install', package])

