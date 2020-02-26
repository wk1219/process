from win32com.client import GetObject
WMI = GetObject('winmgmts:')
arg = input("Input Proc Name : ")
process_ = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % arg)

print(process_[0].Properties_('ProcessId').value)
