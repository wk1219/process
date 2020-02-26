from win32com.client import GetObject
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

