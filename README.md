# LazyPath

a short python script which can backup &amp; restore your PATH environment variable

## Usage
### 1. backup your %PATH%
    python lzEnv.py backup [backup\_file_name]
if no backup\file_name given, will use current time as the name
### 2. restore %PATH% from backups
_run this script with administrator's privilege_

    python lzEnv.py restore backup\_file_name

## other
you can open backup file, edit it directly and then will restore command
