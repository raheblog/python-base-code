#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:38:07 2026

@author: raheb
"""
import random
import string


    
def generate_password(length=10):
    charecters=string.ascii_letters+string.digits+string.punctuation
    password = "".join(random.choice(charecters) for i in range(length))
    print("Generated passwoard:", password)
    
        
length=int(input("Enter passwoard: "))
generate_password()        
    
    
    
    
    
    
    