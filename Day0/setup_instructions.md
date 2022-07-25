---
title: "Getting Started with Python"
author: Benjamin S. Noble
date: 2021-06-30
output: pdf_document
---

# Installing Python 3

## On Mac

1. Download and install Xcode from App Store: [https://developer.apple.com/xcode/](https://developer.apple.com/xcode/)
2. Open Terminal (cmd + space, then type terminal)
3. Install Homebrew by copying and pasting the following command to the Terminal and following the prompts: 

	```
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	```

4. Install Python 3 using the following command line: `brew install python3`
5. Check if Python 3 was correctly installed. Open Terminal, then type: `python3`.
6. (Optional, but highly recommended) Install IPython. Open Terminal, then copy and paste: `pip install ipython`
7.  Check if IPython was correctly installed. Open Terminal, then type: `ipython`

# On Windows 10

You can find a very good tutorial here: https://phoenixnap.com/kb/how-to-install-python-3-windows. Please follow all the steps through step 5. 

# Using Python

There are a number of ways to access Python on your computer. Learn Python the Hard Way will help you use it through the Terminal. I would encourage you to try and get a feel for that and understand how it works. 

However, for those familiar with running code interactively (as in RStudio), you might find the follow resources helpful:

## Sublime Text

Sublime Text is a free text editing program that I highly recommend.^[In addition to Python, you can use Sublime Text to write R code, write RMD files, and even write and compile LaTeX documents. I use it is as my primary LaTeX writer, and would be happy to help you on this front as it makes citations especially easy.] Sublime Text allows you to interactively send code to the terminal and run Python line-by-line, similar to RStudio.

To use Sublime Text for Python...

1. Download and install Sublime Text: https://www.sublimetext.com

## SendCode (Mac)

2. In Sublime Text, use the shortcut cmd + shift + p to open the command palette. Type `install package control` and press enter.
3. Once package control has installed, open the command palette again (cmd + shift + p) and type `package control: install package` and press enter.
4. Then, type `SendCode` and press enter. 

With "SendCode," you will be able to send your code to the Terminal using CMD + Return. It works with both Python and IPython (and also R and RStudio). Unfortunately, there is no support for Windows.

## Send to Shell (Windows)

1. Try "Send to Shell:" https://github.com/Twizzledrizzle/Send-to-Shell. I have never used Send to Shell, but I'm glad to help if you decide to try.

## Spyder

Spyder is basically RStudio, except for Python. Some people prefer Spyder to Sublime Text and Send Code, however the find it to be a bit clunky 😬. To install Spyder:

1. Visit https://docs.anaconda.com/anaconda/install/ and install Anaconda on your system. 
2. Once installed, open Anaconda and install Spyder.

# GitHub

We will be using GitHub to share course materials and homework. If you are not familiar with GitHub, it is an open-source version control website used by programmers and data scientists. You will not need to use GitHub until the class starts (and I will talk more about it). However, in the meantime, you can do the following: 

## Installing GitHub (Mac OS and Windows 10)

1. Go to www.github.com.
2. Create an account.
3. Follow these instructions to install git, the Github coding language (don't worry, we will only need to know a few commands): https://github.com/git-guides/install-git. For Mac users, follow the "homebrew" directions as those will be easiest if you've followed the previous steps in this guide.

I will talk more about using GitHub on the first day of class.

# Create a Twitter Developer Account

One useful skill we'll learn in this class is how to scrape (aka programmatically download and save) Tweets. To do this, however, you'll need a Twitter Developer Account. The process of obtaining an account is somewhat mysterious and can take time. **Please start this process as soon as possible so you have your account before the first day.**

0. Go to twitter.com, and create an account if you don't have one.^[You will not have to use Twitter or Tweet anything at any point (I don't). You must have an account to interact with the API.]
1. Go to developer.twitter.com, and click on Apply. Then, click on Apply for a Developer Account.
3. Choose academic and then student.^[If you are interested in Twitter data in the future, you can apply for an "academic researcher" account. The application process can take longer and is a bit more onerous, so for now, stick with the student account. Once the course ends, I am happy to give advice on the academic research account application and how to use it.]
4. Follow the prompts and fill out the form. Important: DO NOT LIE! You can explain that you will use the API for a Python course to collect data on public figures (politicians and political parties, for example). You may also say that you will not sell the data and that you will use to produce scientific research.
5. You may receive an email from Twitter requesting more details. Repeat your first answer, but add a few more details.
6. You should receive an account after a few days.
7. After receiving your account, click on Apps. Then, click on Create a New App.
8. After creating the app, you click on Details. You will find your keys and tokens under "Keys and Tokens." I will explain how to use these during class.


