from win32com.client import GetObject
import ctypes
cnt = -1
PROCESSES_LIST_ = []
PROCESSES_PID_LIST_ = []
WMI = GetObject('winmgmts:')
process_ = WMI.InstancesOf('Win32_Process')

for ps_ in process_:
    cnt += 1
    PROCESSES_LIST_.append(ps_.Properties_('Name').Value)
    PROCESSES_PID_LIST_.append(ps_.Properties_('ProcessId').value)
    print("Process Name : %s || PID : %s " % (PROCESSES_LIST_[cnt], PROCESSES_PID_LIST_[cnt]))

if ctypes.windll.shell32.IsUserAnAdmin():
    print("Authority : Admin Privilege")
else:
    print("Authority : User Privilege")
print("Total Process : %d" % cnt)
