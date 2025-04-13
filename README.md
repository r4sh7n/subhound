# 🐺 SubHound — Subdomain + Wildcard Detector Tool

![Version](https://img.shields.io/badge/Version-1.0-blue?style=flat-square)
![Python](https://img.shields.io/badge/Made%20With-Python-yellow?style=flat-square)
![Recon Tool](https://img.shields.io/badge/Recon-Subdomain%20Enum%20%26%20Wildcard-critical?style=flat-square)

> Hunt subdomains and detect wildcard DNS entries like a hound.  
> Built for bug bounty hunters, security researchers, and automation lovers. 🕵️

---

## 🧠 Features

- 🚀 Subdomain Enumeration using Sublist3r
- 🧪 Wildcard DNS Detection
- 🛠️ Easy Integration with Recon Workflows
- 💾 Saves output to `subdomains.txt`

---

## 🎯 Usage

```bash
git clone https://github.com/r4sh7n/subhound.git
cd subhound
pip install -r requirements.txt

# Install sublist3r if not already installed
sudo apt install sublist3r

python3 subhound.py
```

---

## 📸 Preview

```
   ____        _     _                     _                 
  / ___| _   _| |__ | |__   ___  _ __   __| | ___ _ __ ___   
  \___ \| | | | '_ \| '_ \ / _ \| '_ \ / _` |/ _ \ '__/ _ \  
   ___) | |_| | |_) | |_) | (_) | | | | (_| |  __/ | | (_) | 
  |____/ \__,_|_.__/|_.__/ \___/|_| |_|\__,_|\___|_|  \___/  

        🔎 SubHound v1.0 — Hunt Subdomains Like a Hound

Enter target domain (e.g. example.com):
```

---

## 📝 Output

- All subdomains saved to `subdomains.txt`
- Wildcard DNS checks printed live to console

---

## 📌 Dependencies

- Python 3.x
- [dnspython](https://pypi.org/project/dnspython/)
- Sublist3r
- requests

---

## 👨‍💻 Author

- Made with ❤️ by [r4sh7n](https://github.com/r4sh7n)

---

## ⚠️ Disclaimer

This tool is for **educational** and **authorized security testing** only. Use responsibly.
