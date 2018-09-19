call ci\set-win-path.bat

powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/limix/chi2comb/master/install.bat', 'install-chi2comb.bat')"