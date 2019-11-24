import psutil
from pathlib import Path

base_path = str(Path(__file__).resolve().parent)

for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'cwd'])  # , name=['geckodriver.exe'])
        order = dict(sorted(pinfo.items()))
        if order.get('name') == 'geckodriver.exe':
            gecko_path = order['cwd']
            print(gecko_path, '\n')
    except psutil.NoSuchProcess:
        pass
    else:
        pass

# returns nothing if the process is not running