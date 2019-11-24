import psutil
import sys
from pathlib import Path

base_path = str(Path(__file__).resolve().parent)

for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'cwd'])#, name=['geckodriver.exe'])
        order = dict(sorted(pinfo.items()))
        if order.get('name') == 'geckodriver.exe':
            gecko_pid = order['pid']
            print(gecko_pid, '\n')
            sys.exit()
            #if gecko_pid == '':
            #    print('no process found')
    except psutil.NoSuchProcess:
        pass
    else: pass

    #sys.exit('No process found')

#returns nothing if the process is not running
