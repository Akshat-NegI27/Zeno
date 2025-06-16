# 
# 🔍Zeno - Multi-Tool Security Reconnaissance and Dork Scanner

A Python-based CLI tool for ethical hackers and security researchers to perform reconnaissance, vulnerability discovery, and directory fuzzing using Google Dorks, CVE databases, and archive lookups.

---

## 📌 Overview

This tool provides a multi-functional interface for discovering security issues in web applications using:

- Google Dorking
- CVE Exploit scraping (via CXSecurity)
- Wayback Machine analysis
- Directory and file fuzzing

> ⚠️ **For educational and authorized testing only. Misuse may violate laws and service terms.**

---

## ⚙️ Modules Used

- `requests`: HTTP request handling
- `BeautifulSoup` (from `bs4`): HTML parsing
- `colorama`: Terminal color formatting
- `os`, `sys`: System control
- `random`, `re`: Randomization and regex parsing

---

## 📁 Features and Functionalities

### 1. 🕵️ Dorker
Searches for vulnerabilities via Google Dorks on a list of domains:
- Directory listing (`intitle:index.of`)
- Exposed config/log/database/backup files
- WordPress fingerprinting
- Subdomains and Wayback Machine artifacts
- Pastebin leaks and LinkedIn employee discovery

### 2. 💥 Exploit Fetcher
- Scrapes the latest CVEs and exploits from [CXSecurity](https://cxsecurity.com/)
- Displays vulnerability descriptions and details

### 3. 🔄 GDork Updater
- Pulls updated dorks from cxsecurity.com
- Performs live Google search for vulnerable URLs using those dorks

### 4. 🧪 Fuzzer
- Uses `list.txt` wordlist to brute-force paths on target URL
- Flags HTTP status codes (e.g., 200, 403, 404)

---

## 🔐 Security and Ethical Considerations

This tool is **strictly for legal use**:
- Use only on assets you own or are authorized to test.
- Excessive Google Dorking may result in temporary bans or violations of Google's terms of service.
- Use proxies, headers, or delay logic responsibly.

---

## 💡 Implementation Notes

- Randomized colors and User-Agent strings to reduce detection.
- HTML parsing via regex on Google's dynamic content is **brittle**.
- Basic connection error handling included, but no retry logic.

---

## 🚀 Possible Improvements

- Use APIs like [NVD](https://nvd.nist.gov/) for CVEs
- Replace scraping with official search APIs (e.g., Bing)
- Support multithreading for faster domain scans
- Export results to CSV/JSON format
- Implement persistent session logging

---

## ✅ Conclusion

This toolkit helps automate routine reconnaissance tasks during early phases of penetration testing. With enhancements and responsible usage, it can save significant time and help identify potential vulnerabilities through public search engines and exploit databases.

---

## 📝 License

This project is for **educational and research purposes** only. Use at your own risk. The authors are **not responsible** for any misuse or damage caused.

