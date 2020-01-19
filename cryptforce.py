#!/usr/bin/python

import crypt

def crackPass(cryptWord):
    salt = cryptWord[0:2]
    dictionary = open('dictionary.txt', 'r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print "[+] Password found: " + word
            return 1 
    return 0

def main():
    passFile = open('pass.txt', 'r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptWord = line.split(":")[1].strip('\n')
            print "[*] Cracking password for: " + user
            if(crackPass(cryptWord)):
                break

main()
            
