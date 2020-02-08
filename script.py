import os, sys

filename = input('File Name...')
path = "C:/Users/ibrah/Documents/VScode/frontend/"


def newfolder():
    os.chdir(path)
    os.mkdir(filename)
    os.chdir(path+filename)
    open('index.html', 'w')
    open('main.css', 'w')
    open('script.js', 'w')


if filename:
    print(newfolder())
