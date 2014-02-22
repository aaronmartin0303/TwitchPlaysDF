#!/usr/bin/env python3

# ircbot.py
# Copyright (C) 2014 : Alex Edwards
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#

import sys
import socket
import string
import os
import time

HOST = "irc.twitch.tv"
PORT = 6667
AUTH = "" #Obtained at http://www.twitchapps.com/tmi 

NICK = "username" 
IDENT = "username"
REALNAME = "username"
MASTER = "username"
CHAT_CHANNEL = "username" #Typically username of the streamer
readbuffer = ""
out = ""
x = 0

os.system("chcp 65001")

s=socket.socket( )
s.connect((HOST, PORT))

s.send(bytes("PASS %s\r\n" % AUTH, "UTF-8"))
s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
s.send(bytes("JOIN #%s\r\n" % CHAT_CHANNEL, "UTF-8"));
s.send(bytes("PRIVMSG #%s :Connected\r\n" % CHAT_CHANNEL, "UTF-8"))

while 1:
    readbuffer = readbuffer+s.recv(1024).decode("UTF-8", errors="ignore")
    temp = str.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        x = 0
        out = ""
        line = str.rstrip(line)
        line = str.split(line)

        for index, i in enumerate(line):
            # I don't know which it is, and I don't care in the slightest
            if(line[index] == "ING: " or line[index] == "ING:" or line[index] 
            == "ING" or line[index] == "PING:" or line[index] == "PING: " or 
            line[index] == "PING"): #PEP8
                s.send(bytes("PONG tmi.twitch.tv\r\n", "UTF-8"))
            if x == 0:
                user = line[index]
                user = user[1:].split('!')[0] + ": "
            if x == 3:
                out += line[index]
                out = out[1:]
            if x >= 4:
                out += " " + line[index]
            x = x + 1
        print(user + out)
        if out.lower() == 'up':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'up')
        if out.lower() == 'right':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'right')
        if out.lower() == 'down':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'down')
        if out.lower() == 'left':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'left')
        if out.lower() == 'enter':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'enter')
        if out.lower() == 'esc':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'esc')
        if out.lower() == 'space':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'space')
        if out == '.':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + '.')
        if out == '>':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + '>')
        if out == ",":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + ",")
        if out == "<":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "<")
        if out == "npne":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npne")
        if out == "npn":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npn")
        if out == "npnw":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npnw")
        if out == "npe":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npe")
        if out == "npc":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npc")
        if out == "npw":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npw")
        if out == "npse":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npse")
        if out == "nps":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "nps")
        if out == "npsw":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "npsw")
        if out == "np0":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "np0")
        if out == "1":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "1")
        if out == "2":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "2")
        if out == "3":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "3")
        if out == "4":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "4")
        if out == "5":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "5")
        if out == "6":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "6")
        if out == "7":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "7")
        if out == "8":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "8")
        if out == "9":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "9")
        if out == "0":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "0")
        if out == "backspace":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "backspace")
        if out == "tab":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "tab")
        if out == "shiftup":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "shiftup")
        if out == "altup":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "altup")
        if out == "shiftright":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "shiftright")
        if out == "altright":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "altright")
        if out == "shiftdown":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "shiftdown")
        if out == "altdown":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "altdown")
        if out == "shiftleft":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "shiftleft")
        if out == "altleft":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "altleft")
        if out == "+":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "+")
        if out == "-":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "-")
        if out == "*":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "*")
        if out == "\\":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "\\")
        if out == "|":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "|")
        if out == "/":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "/")
        if out == "?":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "?")
        if out == "[":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "[")
        #if out == "{":
            #with open("commands.txt", "a") as f:
                #f.write('\n' + user + "{")
        if out == "]":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "]")
        #if out == "}":
            #with open("commands.txt", "a") as f:
                #f.write('\n' + user + "}")
        if out == "f1":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f1")
        if out == "f2":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f2")
        if out == "f3":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f3")
        if out == "f4":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f4")
        if out == "f5":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f5")
        if out == "f6":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f6")
        if out == "f7":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f7")
        if out == "f8":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f8")
        if out == "a":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "a")
        if out == "A":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "A")
        if out == "b":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "b")
        if out == "B":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "B")
        if out == "c":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "c")
        if out == "C":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "C")
        if out == "d":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "d")
        if out == "D":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "D")
        if out == "e":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "e")
        if out == "E":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "E")
        if out == "f":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "f")
        if out == "F":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "F")
        if out == "g":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "g")
        if out == "G":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "G")
        if out == "h":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "h")
        if out == "H":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "H")
        if out == "i":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "i")
        if out == "I":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "I")
        if out == "j":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "j")
        if out == "J":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "J")
        if out == "k":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "k")
        if out == "K":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "K")
        if out == "l":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "l")
        if out == "L":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "L")
        if out == "m":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "m")
        if out == "M":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "M")
        if out == "n":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "n")
        if out == "N":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "N")
        if out == "o":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "o")
        if out == "O":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "O")
        if out == "p":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "p")
        if out == "P":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "P")
        if out == "q":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "q")
        if out == "Q":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "Q")
        if out == "r":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "r")
        if out == "R":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "R")
        if out == "s":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "s")
        if out == "S":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "S")
        if out == "t":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "t")
        if out == "T":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "T")
        if out == "u":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "u")
        if out == "U":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "U")
        if out == "v":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "v")
        if out == "V":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "V")
        if out == "w":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "w")
        if out == "W":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "W")
        if out == "x":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "x")
        if out == "X":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "X")
        if out == "y":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "y")
        if out == "alty":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "alty")
        if out == "Y":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "Y")
        if out == "z":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "z")
        if out == "Z":
            with open("commands.txt", "a") as f:
                f.write('\n' + user + "Z")
