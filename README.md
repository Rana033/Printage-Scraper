# Printage Scraper

Printage Scraper is a Python script designed to scrape books from the Printage website and save them as PDF files. Additionally, it generates QR codes linking to the respective book's URL for easy reference.

## Features

- Scrapes all books from Printage website
- Saves books as PDF files
- Generates QR codes linking to the book's URL

## Technologies
- Web Automation with Selenium WebDriver: Selenium WebDriver is utilized for automating web interactions. It enables navigating through web pages, interacting with dynamic content, and extracting data from websites.
- QR Code Generation with qrcode: The qrcode library facilitates the generation of QR codes, which are essential for linking to the corresponding book URLs within the PDF files.
- PDF Generation with ReportLab: The ReportLab library's canvas module is employed for creating PDF files.
