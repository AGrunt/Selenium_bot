# Selenium_bot

## Prerequisites

* Activated accaunt at Heystack.

## Installation

1. Open console in VSCode.
2. Update system. For ubuntu run: `sudo apt update` 
3. Upgrade system. For ubuntu run: `sudo apt upgrade` 
4. Create virtual environment. Run `python -m venv .venv`
5. Activate virtual environment. Run `source .venv/bin/activate`
6. Install requirements. Run `pip install -r requirements.txt `
7. WebDriver required packages: `ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils`
   For Ubuntu run: `sudo apt install ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils -y`

## How to run

*** Note: Bot works in a chrome application started in incognito with connected Heystack extension. Authentication should be completed manually. 

### Facebook Ad Library
1. Run `python bot.py`
2. Once chrome window opened change `Ad category` to `All ads`, enter category, press Enter.
3. Press button "LOGIN TO HEYSTACK"
4. Login to Heystak.
5. Wait untill Heystak closed.
6. buttons start clicking.


## Testing conditions

Tested under WSL with Ubuntu emulation.

To Brian:
Does not work on another system. Have no time for now to figur out what is wrong. Grate if it works on yours laptop. 