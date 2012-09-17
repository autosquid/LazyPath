import os
import sys
import time
from _winreg import *

def changeWithReg(name,value):
	path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
	reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
	SetValueEx(key,name,0,REG_SZ,value)	


if __name__ == '__main__':
	if sys.argv[1] == 'backup':
		try:
			bk_file = sys.argv[2] 
		except:
			bk_file = time.asctime().replace(' ','_').replace(':','_')+'.backup'
		
		
		with open(bk_file,'w') as f:
			f.write('PATH\n')
			for _p in os.environ['path'].split(';'):
				f.write(_p+'\n')
	elif sys.argv[1] == 'restore':
		try:
			bk_file = sys.argv[2]
		except:
			print('No backup file pointed')
		
		try:
			f = open(bk_file, 'r')
			lines = f.readlines()
			f.close()
			var_name = lines[0].strip()
			for l in lines[1:]:
				value = l.strip()
			var_values = ';'.join([l.strip() for l in lines[1:]])
	
			cmd_line = 'setx '+var_name +' "'+var_values+'" /m'
			if len(cmd_line) < 1024:
				os.system(cmd_line)
			else:
				changeWithReg(var_name,var_values)
		except Exception as e:
			print e
			pass
