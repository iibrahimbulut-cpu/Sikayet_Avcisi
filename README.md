Şikayet Avcısı (Complaint Hunter)
A Python-based web automation tool that scrapes complaint data from Sikayetvar.com via Google Search. It is designed to track brand reputation and monitor specific customer pain points by searching for targeted keywords.

Key Features
Google Dorking Integration: Uses the site:sikayetvar.com operator to filter results directly from Google for maximum efficiency.
Selenium Automation: Leverages Selenium with anti-detection headers (AutomationControlled) to mimic human behavior and reduce the risk of CAPTCHAs.
Batch Processing: Processes a list of keywords in one go, searching for each and collecting the relevant complaint titles and URLs.
Data Export: Automatically saves all findings into a clean Excel (.xlsx) file for further analysis.
Human-Like Interaction: Implements random sleep intervals and custom Chrome options to avoid being flagged as a bot.

Installation
1. Prerequisites
Python 3.x
Google Chrome Browser installed

2. Install Dependencies
Bash
pip install selenium webdriver-manager pandas openpyxl

How to Use
Configure Keywords: Open sikayet_avcisi.py and update the keywords list at the bottom of the file:

Python
keywords = ["garanti bankası", "kredi kartı aidatı", "mobil şube hatası"]

Run the Script:
Bash
python sikayet_avcisi.py

Monitor: The script will open a Chrome window, perform the searches, and print the progress in the terminal.

Get Results: Once finished, look for sikayetvar_garanti_sonuc.xlsx in your project folder.

Technical Details
Engine: Selenium WebDriver with ChromeDriverManager.
Detection Evasion: * disable-blink-features=AutomationControlled
excludeSwitches: enable-automation
Search Logic: It specifically targets the <h3> tags in Google search results and extracts the href links pointing to sikayetvar.com.
Data Handling: Uses pandas to structure the scraped data (Keyword, Title, Link).

⚠️ Important Disclaimer
This tool is for educational and research purposes only. Please ensure you comply with the Terms of Service of both Google and Sikayetvar while using this script. Frequent or high-volume requests may lead to temporary IP blocks or CAPTCHA challenges.
