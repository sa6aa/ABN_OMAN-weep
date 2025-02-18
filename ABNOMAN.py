#!/bin/bash

# تثبيت الإعتمادات الأساسية
install_dependencies() {
    echo "جارٍ تثبيت الإعتمادات الأساسية..."
    sudo apt update -y
    sudo apt install -y git python3 python3-pip curl wget zenity
}

# تثبيت Ettercap (MiTM Attack)
install_ettercap() {
    echo "جارٍ تثبيت Ettercap..."
    sudo apt install -y ettercap-graphical
}

# تثبيت Autosploit (Shodan + Metasploit)
install_autosploit() {
    echo "جارٍ تثبيت Autosploit..."
    git clone https://github.com/NullArray/Autosploit.git
    cd Autosploit
    sudo ./install.sh
    cd ..
}

# تثبيت HackTools (Firefox Extension)
install_hacktools() {
    echo "جارٍ تثبيت HackTools..."
    firefox "https://addons.mozilla.org/en-US/firefox/addon/hacktools/" &
}

# تثبيت Kali Linux Tools
install_kali_tools() {
    echo "جارٍ تثبيت Kali Linux Tools..."
    sudo apt install -y kali-linux-default
}

# تثبيت Fawkes (SQLi Scanner)
install_fawkes() {
    echo "جارٍ تثبيت Fawkes..."
    git clone https://github.com/keegancsmith/sqlfuzz.git
    cd sqlfuzz
    sudo go build
    cd ..
}

# تثبيت Headi (Web Server Exploits)
install_headi() {
    echo "جارٍ تثبيت Headi..."
    git clone https://github.com/mephux/headi.git
    cd headi
    make
    cd ..
}

# تثبيت Nmap (Network Scanner)
install_nmap() {
    echo "جارٍ تثبيت Nmap..."
    sudo apt install -y nmap
}

# تثبيت Nikto (Web Server Scanner)
install_nikto() {
    echo "جارٍ تثبيت Nikto..."
    sudo apt install -y nikto
}

# تثبيت Hydra (Password Cracker)
install_hydra() {
    echo "جارٍ تثبيت Hydra..."
    sudo apt install -y hydra
}

# تثبيت SQLMap (SQL Injection Tool)
install_sqlmap() {
    echo "جارٍ تثبيت SQLMap..."
    sudo apt install -y sqlmap
}

# تثبيت Metasploit Framework
install_metasploit() {
    echo "جارٍ تثبيت Metasploit Framework..."
    curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfupdate | sudo bash
}

# تثبيت John the Ripper (Password Cracker)
install_john() {
    echo "جارٍ تثبيت John the Ripper..."
    sudo apt install -y john
}

# تثبيت Aircrack-ng (WiFi Cracking)
install_aircrack() {
    echo "جارٍ تثبيت Aircrack-ng..."
    sudo apt install -y aircrack-ng
}

# تثبيت Burp Suite (Web Vulnerability Scanner)
install_burpsuite() {
    echo "جارٍ تثبيت Burp Suite..."
    sudo apt install -y burpsuite
}

# تثبيت Wireshark (Network Protocol Analyzer)
install_wireshark() {
    echo "جارٍ تثبيت Wireshark..."
    sudo apt install -y wireshark
}

# تثبيت Social Engineering Toolkit (SET)
install_set() {
    echo "جارٍ تثبيت Social Engineering Toolkit..."
    git clone https://github.com/trustedsec/social-engineer-toolkit.git
    cd social-engineer-toolkit
    sudo python3 setup.py install
    cd ..
}

# تثبيت OWASP ZAP (Web Application Security Scanner)
install_owasp_zap() {
    echo "جارٍ تثبيت OWASP ZAP..."
    sudo apt install -y zaproxy
}

# تثبيت WPScan (WordPress Vulnerability Scanner)
install_wpscan() {
    echo "جارٍ تثبيت WPScan..."
    sudo apt install -y wpscan
}

# تثبيت BeEF (Browser Exploitation Framework)
install_beef() {
    echo "جارٍ تثبيت BeEF..."
    sudo apt install -y beef-xss
}

# تثبيت Arachni (Web Application Security Scanner)
install_arachni() {
    echo "جارٍ تثبيت Arachni..."
    sudo apt install -y arachni
}

# تثبيت Fierce (DNS Scanner)
install_fierce() {
    echo "جارٍ تثبيت Fierce..."
    sudo apt install -y fierce
}

# تثبيت Maltego (Information Gathering)
install_maltego() {
    echo "جارٍ تثبيت Maltego..."
    sudo apt install -y maltego
}

# تثبيت Recon-ng (Web Reconnaissance)
install_reconng() {
    echo "جارٍ تثبيت Recon-ng..."
    sudo apt install -y recon-ng
}

# تثبيت Sublist3r (Subdomain Enumeration)
install_sublist3r() {
    echo "جارٍ تثبيت Sublist3r..."
    git clone https://github.com/aboul3la/Sublist3r.git
    cd Sublist3r
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت TheHarvester (Email, Subdomain and IP gathering)
install_theharvester() {
    echo "جارٍ تثبيت TheHarvester..."
    sudo apt install -y theharvester
}

# تثبيت DirBuster (Directory/File Brute-forcer)
install_dirbuster() {
    echo "جارٍ تثبيت DirBuster..."
    sudo apt install -y dirbuster
}

# تثبيت Gobuster (Directory/File Brute-forcer)
install_gobuster() {
    echo "جارٍ تثبيت Gobuster..."
    sudo apt install -y gobuster
}

# تثبيت Wapiti (Web Vulnerability Scanner)
install_wapiti() {
    echo "جارٍ تثبيت Wapiti..."
    sudo apt install -y wapiti
}

# تثبيت Netsparker (Web Application Security Scanner)
install_netsparker() {
    echo "جارٍ تثبيت Netsparker..."
    sudo apt install -y netsparker
}

# تثبيت A2SV (Auto Scanning for SSL Vulnerabilities)
install_a2sv() {
    echo "جارٍ تثبيت A2SV..."
    git clone https://github.com/hahwul/a2sv.git
    cd a2sv
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Pompem (Exploit Finder)
install_pompem() {
    echo "جارٍ تثبيت Pompem..."
    git clone https://github.com/rfunix/Pompem.git
    cd Pompem
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Sn1per (Automated Pentest Recon Scanner)
install_sn1per() {
    echo "جارٍ تثبيت Sn1per..."
    git clone https://github.com/1N3/Sn1per.git
    cd Sn1per
    sudo ./install.sh
    cd ..
}

# تثبيت D-TECT (All-In-One Tool)
install_dtect() {
    echo "جارٍ تثبيت D-TECT..."
    git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git
    cd D-TECT-1
    sudo chmod +x d-tect.py
    cd ..
}

# تثبيت XSStrike (XSS Detection Suite)
install_xsstrike() {
    echo "جارٍ تثبيت XSStrike..."
    git clone https://github.com/s0md3v/XSStrike.git
    cd XSStrike
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Commix (Command Injection Exploiter)
install_commix() {
    echo "جارٍ تثبيت Commix..."
    git clone https://github.com/commixproject/commix.git
    cd commix
    sudo ./commix.py --install
    cd ..
}

# تثبيت BruteX (Brute Force Attack Tool)
install_brutex() {
    echo "جارٍ تثبيت BruteX..."
    git clone https://github.com/1N3/BruteX.git
    cd BruteX
    chmod +x install.sh
    sudo ./install.sh
    cd ..
}

# تثبيت LazyKali (Kali Automation Tool)
install_lazykali() {
    echo "جارٍ تثبيت LazyKali..."
    git clone https://github.com/noob-hackers/hackers-tool-kit.git
    cd hackers-tool-kit
    sudo ./lazy.sh
    cd ..
}

# تثبيت Crips (Information Gathering Tool)
install_crips() {
    echo "جارٍ تثبيت Crips..."
    git clone https://github.com/Manisso/Crips.git
    cd Crips
    sudo chmod +x crips.py
    cd ..
}

# تثبيت RED_HAWK (All in One Tool)
install_redhawk() {
    echo "جارٍ تثبيت RED_HAWK..."
    git clone https://github.com/Tuhinshubhra/RED_HAWK.git
    cd RED_HAWK
    sudo chmod +x rhawk.php
    cd ..
}

# تثبيت SQLiv (Dorking and SQL Injection Tool)
install_sqliv() {
    echo "جارٍ تثبيت SQLiv..."
    git clone https://github.com/Hadesy2k/sqliv.git
    cd sqliv
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Nishang (PowerShell for Pentesters)
install_nishang() {
    echo "جارٍ تثبيت Nishang..."
    git clone https://github.com/samratashok/nishang.git
    cd nishang
    sudo chmod +x *.ps1
    cd ..
}

# تثبيت ShellShock (Shellshock Exploit Detector)
install_shellshock() {
    echo "جارٍ تثبيت ShellShock..."
    git clone https://github.com/mubix/shellshocker-pocs.git
    cd shellshocker-pocs
    sudo chmod +x shellshocker.sh
    cd ..
}

# تثبيت Yuki-Chan (Automated Penetration Testing Tool)
install_yukichan() {
    echo "جارٍ تثبيت Yuki-Chan..."
    git clone https://github.com/Yukinoshita47/Yuki-Chan-The-Auto-Pentest.git
    cd Yuki-Chan-The-Auto-Pentest
    sudo chmod +x yuki.sh
    cd ..
}

# تثبيت Evil-Droid (Android Framework)
install_evildroid() {
    echo "جارٍ تثبيت Evil-Droid..."
    git clone https://github.com/M4sc3r4n0/Evil-Droid.git
    cd Evil-Droid
    sudo chmod +x evil-droid
    cd ..
}

# تثبيت Katoolin (Kali Linux Tool Installer)
install_katoolin() {
    echo "جارٍ تثبيت Katoolin..."
    git clone https://github.com/LionSec/katoolin.git
    cd katoolin
    sudo chmod +x katoolin.py
    cd ..
}

# تثبيت XAttacker (Website Vulnerability Scanner)
install_xattacker() {
    echo "جارٍ تثبيت XAttacker..."
    git clone https://github.com/Moham3dRiahi/XAttacker.git
    cd XAttacker
    sudo chmod +x XAttacker.pl
    cd ..
}

# تثبيت AndroBugs (Android Vulnerability Scanner)
install_androbugs() {
    echo "جارٍ تثبيت AndroBugs..."
    git clone https://github.com/AndroBugs/AndroBugs_Framework.git
    cd AndroBugs_Framework
    sudo chmod +x androbugs.py
    cd ..
}

# تثبيت Infoga (Email Information Gathering)
install_infoga() {
    echo "جارٍ تثبيت Infoga..."
    git clone https://github.com/m4ll0k/Infoga.git
    cd Infoga
    sudo python3 setup.py install
    cd ..
}

# تثبيت KnockPy (Subdomain Scanner)
install_knockpy() {
    echo "جارٍ تثبيت KnockPy..."
    git clone https://github.com/guelfoweb/knock.git
    cd knock
    sudo python3 setup.py install
    cd ..
}

# تثبيت Morpheus (Man-In-The-Middle Attack Framework)
install_morpheus() {
    echo "جارٍ تثبيت Morpheus..."
    git clone https://github.com/r00t-3xp10it/morpheus.git
    cd morpheus
    sudo chmod +x morpheus.sh
    cd ..
}

# تثبيت ReconDog (Information Gathering Tool)
install_recondog() {
    echo "جارٍ تثبيت ReconDog..."
    git clone https://github.com/UltimateHackers/ReconDog.git
    cd ReconDog
    sudo chmod +x dog
    cd ..
}

# تثبيت Striker (Recon & Vulnerability Scanning Suite)
install_striker() {
    echo "جارٍ تثبيت Striker..."
    git clone https://github.com/s0md3v/Striker.git
    cd Striker
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Zarp (Network Attack Tool)
install_zarp() {
    echo "جارٍ تثبيت Zarp..."
    git clone https://github.com/hatRiot/zarp.git
    cd zarp
    sudo python3 setup.py install
    cd ..
}

# تثبيت Zphisher (Phishing Tool)
install_zphisher() {
    echo "جارٍ تثبيت Zphisher..."
    git clone https://github.com/htr-tech/zphisher.git
    cd zphisher
    sudo chmod +x zphisher.sh
    cd ..
}

# تثبيت Fuxploider (File Upload Vulnerability Scanner)
install_fuxploider() {
    echo "جارٍ تثبيت Fuxploider..."
    git clone https://github.com/almandin/fuxploider.git
    cd fuxploider
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت CMSmap (CMS Scanner)
install_cmsmap() {
    echo "جارٍ تثبيت CMSmap..."
    git clone https://github.com/Dionach/CMSmap.git
    cd CMSmap
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت CMSScanner (CMS Vulnerability Scanner)
install_cmsscanner() {
    echo "جارٍ تثبيت CMSScanner..."
    git clone https://github.com/wpscanteam/CMSScanner.git
    cd CMSScanner
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Smbmap (SMB Enumeration Tool)
install_smbmap() {
    echo "جارٍ تثبيت Smbmap..."
    git clone https://github.com/ShawnDEvans/smbmap.git
    cd smbmap
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت AutoRecon (Multi-Purpose Recon Tool)
install_autorecon() {
    echo "جارٍ تثبيت AutoRecon..."
    git clone https://github.com/Tib3rius/AutoRecon.git
    cd AutoRecon
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Osmedeus (Automated Recon Tool)
install_osmedeus() {
    echo "جارٍ تثبيت Osmedeus..."
    git clone https://github.com/j3ssie/Osmedeus.git
    cd Osmedeus
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت SprayingToolkit (Credential Stuffing Toolkit)
install_sprayingtoolkit() {
    echo "جارٍ تثبيت SprayingToolkit..."
    git clone https://github.com/byt3bl33d3r/SprayingToolkit.git
    cd SprayingToolkit
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Droopescan (Drupal Vulnerability Scanner)
install_droopescan() {
    echo "جارٍ تثبيت Droopescan..."
    git clone https://github.com/droope/droopescan.git
    cd droopescan
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت CrackMapExec (Post-Exploitation Tool)
install_crackmapexec() {
    echo "جارٍ تثبيت CrackMapExec..."
    git clone https://github.com/byt3bl33d3r/CrackMapExec.git
    cd CrackMapExec
    sudo python3 setup.py install
    cd ..
}
# تثبيت PowerSploit (PowerShell Post-Exploitation Framework)
install_powersploit() {
    echo "جارٍ تثبيت PowerSploit..."
    git clone https://github.com/PowerShellMafia/PowerSploit.git
    cd PowerSploit
    sudo chmod +x *.ps1
    cd ..
}

# تثبيت SPARTA (Network Infrastructure Penetration Testing Tool)
install_sparta() {
    echo "جارٍ تثبيت SPARTA..."
    git clone https://github.com/SECFORCE/sparta.git
    cd sparta
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت SpiderFoot (OSINT Automation Tool)
install_spiderfoot() {
    echo "جارٍ تثبيت SpiderFoot..."
    git clone https://github.com/smicallef/spiderfoot.git
    cd spiderfoot
    sudo python3 setup.py install
    cd ..
}

# تثبيت TIDoS Framework (Web Penetration Testing Tool)
install_tidos() {
    echo "جارٍ تثبيت TIDoS Framework..."
    git clone https://github.com/0xInfection/TIDoS-Framework.git
    cd TIDoS-Framework
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت XSpear (XSS Detection Tool)
install_xspear() {
    echo "جارٍ تثبيت XSpear..."
    git clone https://github.com/hahwul/XSpear.git
    cd XSpear
    sudo gem install XSpear
    cd ..
}

# تثبيت Drozer (Android Security Testing Tool)
install_drozer() {
    echo "جارٍ تثبيت Drozer..."
    git clone https://github.com/FSecureLABS/drozer.git
    cd drozer
    sudo ./install.sh
    cd ..
}

# تثبيت Skiptracer (OSINT Tool)
install_skiptracer() {
    echo "جارٍ تثبيت Skiptracer..."
    git clone https://github.com/xillwillx/skiptracer.git
    cd skiptracer
    sudo pip3 install -r requirements.txt
    cd ..
}

# تثبيت Sifter (OSINT, Recon & Vulnerability Scanning Suite)
install_sifter() {
    echo "جارٍ تثبيت Sifter..."
    git clone https://github.com/s1l3nt78/sifter.git
    cd sifter
    sudo chmod +x install.sh
    sudo ./install.sh
    cd ..
}

# تثبيت InstantEX (Exploit Finder)
install_instanex() {
    echo "جارٍ تثبيت InstantEX..."
    git clone https://github.com/nyxgeek/InstantEX.git
    cd InstantEX
    sudo pip3 install -r requirements.txt
    cd ..
}

# تنفيذ التثبيت
show_menu() {
    choice=$(zenity --list --title="ABN_OMAN Pentest-Tools" --text="اختر الأداة التي تريد تثبيتها:" --column="رقم" --column="الأداة" \
        1 "Ettercap (MiTM Attack)" \
        2 "Autosploit (Shodan + Metasploit)" \
        3 "HackTools (Firefox Extension)" \
        4 "Kali Linux Tools" \
        5 "Fawkes (SQLi Scanner)" \
        6 "Headi (Web Server Exploits)" \
        7 "Nmap (Network Scanner)" \
        8 "Nikto (Web Server Scanner)" \
        9 "Hydra (Password Cracker)" \
        10 "SQLMap (SQL Injection Tool)" \
        11 "Metasploit Framework" \
        12 "John the Ripper (Password Cracker)" \
        13 "Aircrack-ng (WiFi Cracking)" \
        14 "Burp Suite (Web Vulnerability Scanner)" \
        15 "Wireshark (Network Protocol Analyzer)" \
        16 "Social Engineering Toolkit (SET)" \
        17 "OWASP ZAP (Web Application Security Scanner)" \
        18 "WPScan (WordPress Vulnerability Scanner)" \
        19 "BeEF (Browser Exploitation Framework)" \
        20 "Arachni (Web Application Security Scanner)" \
        21 "Fierce (DNS Scanner)" \
        22 "Maltego (Information Gathering)" \
        23 "Recon-ng (Web Reconnaissance)" \
        24 "Sublist3r (Subdomain Enumeration)" \
        25 "TheHarvester (Email, Subdomain and IP gathering)" \
        26 "DirBuster (Directory/File Brute-forcer)" \
        27 "Gobuster (Directory/File Brute-forcer)" \
        28 "Wapiti (Web Vulnerability Scanner)" \
        29 "Netsparker (Web Application Security Scanner)" \
        30 "A2SV (Auto Scanning for SSL Vulnerabilities)" \
        31 "Pompem (Exploit Finder)" \
        32 "Sn1per (Automated Pentest Recon Scanner)" \
        33 "D-TECT (All-In-One Tool)" \
        34 "XSStrike (XSS Detection Suite)" \
        35 "Commix (Command Injection Exploiter)" \
        36 "BruteX (Brute Force Attack Tool)" \
        37 "LazyKali (Kali Automation Tool)" \
        38 "Crips (Information Gathering Tool)" \
        39 "RED_HAWK (All in One Tool)" \
        40 "SQLiv (Dorking and SQL Injection Tool)" \
        41 "Nishang (PowerShell for Pentesters)" \
        42 "ShellShock (Shellshock Exploit Detector)" \
        43 "Yuki-Chan (Automated Penetration Testing Tool)" \
        44 "Evil-Droid (Android Framework)" \
        45 "Katoolin (Kali Linux Tool Installer)" \
        46 "XAttacker (Website Vulnerability Scanner)" \
        47 "AndroBugs (Android Vulnerability Scanner)" \
        48 "Infoga (Email Information Gathering)" \
        49 "KnockPy (Subdomain Scanner)" \
        50 "Morpheus (Man-In-The-Middle Attack Framework)" \
        51 "ReconDog (Information Gathering Tool)" \
        52 "Striker (Recon & Vulnerability Scanning Suite)" \
        53 "Zarp (Network Attack Tool)" \
        54 "Zphisher (Phishing Tool)" \
        55 "Fuxploider (File Upload Vulnerability Scanner)" \
        56 "CMSmap (CMS Scanner)" \
        57 "CMSScanner (CMS Vulnerability Scanner)" \
        58 "Smbmap (SMB Enumeration Tool)" \
        59 "AutoRecon (Multi-Purpose Recon Tool)" \
        60 "Osmedeus (Automated Recon Tool)" \
        61 "SprayingToolkit (Credential Stuffing Toolkit)" \
        62 "Droopescan (Drupal Vulnerability Scanner)" \
        63 "CrackMapExec (Post-Exploitation Tool)" \
        64 "PowerSploit (PowerShell Post-Exploitation Framework)" \
        65 "SPARTA (Network Infrastructure Penetration Testing Tool)" \
        66 "SpiderFoot (OSINT Automation Tool)" \
        67 "TIDoS Framework (Web Penetration Testing Tool)" \
        68 "XSpear (XSS Detection Tool)" \
        69 "Drozer (Android Security Testing Tool)" \
        70 "Skiptracer (OSINT Tool)" \
        71 "Sifter (OSINT, Recon & Vulnerability Scanning Suite)" \
        72 "InstantEX (Exploit Finder)" \
        0 "Exit")

    case $choice in
        1) install_ettercap ;;
        2) install_autosploit ;;
        3) install_hacktools ;;
        4) install_kali_tools ;;
        5) install_fawkes ;;
        6) install_headi ;;
        7) install_nmap ;;
        8) install_nikto ;;
        9) install_hydra ;;
        10) install_sqlmap ;;
        11) install_metasploit ;;
        12) install_john ;;
        13) install_aircrack ;;
        14) install_burpsuite ;;
        15) install_wireshark ;;
        16) install_set ;;
        17) install_owasp_zap ;;
        18) install_wpscan ;;
        19) install_beef ;;
        20) install_arachni ;;
        21) install_fierce ;;
        22) install_maltego ;;
        23) install_reconng ;;
        24) install_sublist3r ;;
        25) install_theharvester ;;
        26) install_dirbuster ;;
        27) install_gobuster ;;
        28) install_wapiti ;;
        29) install_netsparker ;;
        30) install_a2sv ;;
        31) install_pompem ;;
        32) install_sn1per ;;
        33) install_dtect ;;
        34) install_xsstrike ;;
        35) install_commix ;;
        36) install_brutex ;;
        37) install_lazykali ;;
        38) install_crips ;;
        39) install_redhawk ;;
        40) install_sqliv ;;
        41) install_nishang ;;
        42) install_shellshock ;;
        43) install_yukichan ;;
        44) install_evildroid ;;
        45) install_katoolin ;;
        46) install_xattacker ;;
        47) install_androbugs ;;
        48) install_infoga ;;
        49) install_knockpy ;;
        50) install_morpheus ;;
        51) install_recondog ;;
        52) install_striker ;;
        53) install_zarp ;;
        54) install_zphisher ;;
        55) install_fuxploider ;;
        56) install_cmsmap ;;
        57) install_cmsscanner ;;
        58) install_smbmap ;;
        59) install_autorecon ;;
        60) install_osmedeus ;;
        61) install_sprayingtoolkit ;;
        62) install_droopescan ;;
        63) install_crackmapexec ;;
        64) install_powersploit ;;
        65) install_sparta ;;
        66) install_spiderfoot ;;
        67) install_tidos ;;
        68) install_xspear ;;
        69) install_drozer ;;
        70) install_skiptracer ;;
        71) install_sifter ;;
        72) install_instanex ;;
        0) exit 0 ;;
        *) zenity --error --text="خيار غير صالح. يرجى الاختيار مرة أخرى." ;;
    esac
}

# Main script
install_dependencies
while true; do
    show_menu
done
