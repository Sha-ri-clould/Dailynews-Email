# What is this project?
### This Python script fetches the latest popular news articles related to Apple from the NewsAPI, formats their titles and descriptions, and sends them to your email inbox.

## Features
### Fetches news articles using the NewsAPI for a specific keyword.
### Formats and compiles the titles and descriptions of all retrieved articles.
### Sends the news summary via email using secure SMTP.
### Uses environment variables for email credentials for added security.

## How to use?
### Import requests, smtplib, ssl, email.message, os library.
### Add required news category url from NewsAPI.
### Add sender email, receiver email, password.
