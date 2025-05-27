# Confaz Registration Automation

## Overview

This tool is designed to streamline the unification of monthly CONFAZ registration records into a single, well-formatted Excel file. It automates the collection, processing, and consolidation of registration data across multiple months, significantly reducing manual effort and saving time.

## Features

- Automatically collects registration records for all months  
- Merges data into one comprehensive Excel spreadsheet  
- User-friendly and easy to configure  
- Saves time by eliminating manual data merging 

## Usage

1. Choose the main file that contains all the existing CONFAZ registration records.  
2. Select the folder with the new month's registration files.  
3. Enter the month and year of the new records.  
4. Click the update button to process the data.  
5. The tool will generate a unified Excel file that preserves the original formatting, combining all months' records into one.

## Requirements

- Required libraries:
  - flet >= 0.28.3  
  - ipykernel >= 6.29.5  
  - openpyxl >= 3.1.5  
  - pandas >= 2.2.3  
  - ruff >= 0.11.10  
  - xlrd >= 2.0.1  
  - flet-cli == 0.28.3  
  - flet-desktop == 0.28.3  
  - pyinstaller >= 6.13.0  

## Installation

```bash
git clone https://github.com/yourusername/confaz-registration-automation.git
cd confaz-registration-automation
pip install uv
uv install
uv sync
