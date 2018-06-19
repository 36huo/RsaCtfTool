#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# author: 36huo
# ------------------------------------------------
# RsaCtfTools  help script 

import subprocess
import os
import libnum
import gmpy 

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

print("""What you have:
1: public_key_file & ciphered_file
2: n,e,c 
3: p q e c
4: d e c
""")
input_num=raw_input("choice:")
if input_num=='1':
    public_key_file=raw_input("public key filename=")
    ciphered_file=raw_input("ciphered filename=")
    command_str="python RsaCtfTool.py --publickey {} --uncipherfile {} --verbos".format(os.path.join(BASE_PATH, public_key_file),os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)
    print("[*] Performing private keyfile")
    command_str="python RsaCtfTool.py --publickey {} --private > pri.key".format(os.path.join(BASE_PATH, public_key_file))
    os.system(command_str)
    print("[*] private keyfile: pri.key")
    # command_str="python RsaCtfTool.py --dumpkey --key pri.key"
    # os.system(command_str)
    print("[*] using openssl decrypt pkcs\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -pkcs && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)
    print("\n[*] using openssl decrypt oaep\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -oaep && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)
    print("\n[*] using openssl decrypt ssl\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -ssl && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)
    print("\n[*] using openssl decrypt raw\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -raw && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)


elif input_num=='2':
    n=input("n=")
    e=input("e=")
    c=input("c=")
    command_str="python RsaCtfTool.py  -n {} -e {} --uncipher {} --verbose".format(n,e,c)
    os.system(command_str)
    print("\n[*] Performing pubile keyfile")
    command_str="python RsaCtfTool.py --createpub -n {} -e {} --uncipher {} > pub.key ".format(n,e,c)
    os.system(command_str)
    print("[*] private keyfile: pub.key")
    public_key_file="pub.key"
    print("[*] Performing private keyfile")
    command_str="python RsaCtfTool.py --publickey {} --private > pri.key".format(os.path.join(BASE_PATH, public_key_file))
    os.system(command_str)
    print("[*] private keyfile: pri.key")

    with open("ciphered_file",'wb') as f:
        f.write(libnum.n2s(c))
    ciphered_file="ciphered_file"
    print("[*] using openssl decrypt pkcs\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -pkcs && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)
    print("\n[*] using openssl decrypt oaep\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -oaep && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)
    print("\n[*] using openssl decrypt ssl\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -ssl && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)
    print("\n[*] using openssl decrypt raw\n")
    command_str="openssl rsautl -decrypt -in {} -inkey pri.key -out m.txt -raw && cat m.txt".format(os.path.join(BASE_PATH, ciphered_file))
    os.system(command_str)

elif input_num=='3':
    p=input("p=")
    q=input("q=")
    e=input("e=")
    c=input("c=")
    n=p*q
    t=(p-1)*(q-1)
    d=gmpy.invert(e,t)
    m=pow(c,d,n)
    print(libnum.n2s(m))
    
elif input_num=='4':   
    # p=input("p=")
    # q=input("q=")
    # e=input("e=")
    # c=input("c=")
    # n=p*q
    # t=(p-1)*(q-1)
    # d=gmpy.invert(e,t)
    # m=pow(c,d,n)
    # print(libnum.n2s(m))

else:
    print("input error")
    exit()
