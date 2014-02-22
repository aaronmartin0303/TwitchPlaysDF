#!/usr/bin/env python3

# controller.py
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

import time, os, win32com.client, win32api, win32con

loop = False

############## Initialization of command variables
enter_c = 0
esc_c = 0
space_c = 0 #advance/clear messages
stop_c = 0 # stop meaning "."
shiftstop_c = 0 #descend or ctrl + numpad5
comma_c = 0
shiftcomma_c = 0 #ascend or shift + numpad5
numpad9_c = 0
numpad8_c = 0
numpad7_c = 0
numpad6_c = 0
numpad5_c = 0
numpad4_c = 0
numpad3_c = 0
numpad2_c = 0
numpad1_c = 0
numpad0_c = 0
one_c = 0
two_c = 0
three_c = 0
four_c = 0
five_c = 0
six_c = 0
seven_c = 0
eight_c = 0
nine_c = 0
zero_c = 0
backspace_c = 0
tab_c = 0
up_c = 0 #move or attack directionally
shiftup_c = 0 #move cursor faster
altup_c = 0 #move carefully
right_c = 0
shiftright_c = 0
altright_c = 0
down_c = 0
shiftdown_c = 0
altdown_c = 0
left_c = 0
shiftleft_c = 0
altleft_c = 0
plus_c = 0
minus_c = 0
asterisk_c = 0
backslash_c = 0
shiftbackslash_c = 0 #|
slash_c = 0
shiftslash_c = 0 #?
leftbracket_c = 0 #[
leftshiftbracket_c = 0 #{
rightbracket_c = 0 #]
rightshiftbracket_c = 0 #}
f1_c = 0
f2_c = 0
f3_c = 0
f4_c = 0
f5_c = 0
f6_c = 0
f7_c = 0
f8_c = 0
a_c = 0 #view announcements
shiftA_c = 0
b_c = 0
shiftB_c = 0
c_c = 0 #view companion interface
shiftC_c = 0 #combat preferences interface
d_c = 0 #drop an item
shiftD_c = 0 #Date/time
e_c = 0 #eat!
shiftE_c = 0
f_c = 0 #fires a projectile
shiftF_c = 0
g_c = 0 #pick up an item
shiftG_c = 0
h_c = 0
shiftH_c = 0
i_c = 0 #inventory
shiftI_c = 0 #interact with object in inventory
j_c = 0
shiftJ_c = 0
k_c = 0 #talks to somebody
shiftK_c = 0
l_c = 0 #looks around
shiftL_c = 0 #searches very carefully (chance of finding small creatures)
m_c = 0
shiftM_c = 0
n_c = 0
shiftN_c = 0
o_c = 0
shiftO_c = 0
p_c = 0 #put item in container
shiftP_c = 0 #temPerature!
q_c = 0
shiftQ_c = 0 #View Quest log
r_c = 0 #remove item being worn or from a container
shiftR_c = 0
s_c = 0 #stand or lie down, also used for crawling past npcs
shiftS_c = 0 #Sneak
t_c = 0 #throws an item
shiftT_c = 0 #Fast Travel
u_c = 0 #interact with building furniture or mechanism
shiftU_c = 0
v_c = 0
shiftV_c = 0
w_c = 0 #wear an item
'''If you want to get a specific item from your backpack to your right hand 
(wield weapon): 1) drop current item from right hand, 2) [r]emove wanted item 
from backpack, 3) pick up wanted item.'''
shiftW_c = 0 #Weather
x_c = 0 #perform action, butcher, create, etc.
shiftX_c = 0
y_c = 0
shiftY_c = 0
z_c = 0 #status
shiftZ_c = 0 #sleep
##############

shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("DwarfFortress.exe")

VK_CODE = {'backspace':0x08,
                    'tab':0x09,
                    'clear':0x0C,
                    'enter':0x0D,
                    'shift':0x10,
                    'ctrl':0x11,
                    'alt':0x12,
                    'pause':0x13,
                    'caps_lock':0x14,
                    'esc':0x1B,
                    'spacebar':0x20,
                    'page_up':0x21,
                    'page_down':0x22,
                    'end':0x23,
                    'home':0x24,
                    'left_arrow':0x25,
                    'up_arrow':0x26,
                    'right_arrow':0x27,
                    'down_arrow':0x28,
                    'select':0x29,
                    'print':0x2A,
                    'execute':0x2B,
                    'print_screen':0x2C,
                    'ins':0x2D,
                    'del':0x2E,
                    'help':0x2F,
                    '0':0x30,
                    '1':0x31,
                    '2':0x32,
                    '3':0x33,
                    '4':0x34,
                    '5':0x35,
                    '6':0x36,
                    '7':0x37,
                    '8':0x38,
                    '9':0x39,
                    'a':0x41,
                    'b':0x42,
                    'c':0x43,
                    'd':0x44,
                    'e':0x45,
                    'f':0x46,
                    'g':0x47,
                    'h':0x48,
                    'i':0x49,
                    'j':0x4A,
                    'k':0x4B,
                    'l':0x4C,
                    'm':0x4D,
                    'n':0x4E,
                    'o':0x4F,
                    'p':0x50,
                    'q':0x51,
                    'r':0x52,
                    's':0x53,
                    't':0x54,
                    'u':0x55,
                    'v':0x56,
                    'w':0x57,
                    'x':0x58,
                    'y':0x59,
                    'z':0x5A,
                    'numpad_0':0x60,
                    'numpad_1':0x61,
                    'numpad_2':0x62,
                    'numpad_3':0x63,
                    'numpad_4':0x64,
                    'numpad_5':0x65,
                    'numpad_6':0x66,
                    'numpad_7':0x67,
                    'numpad_8':0x68,
                    'numpad_9':0x69,
                    'multiply_key':0x6A,
                    'add_key':0x6B,
                    'separator_key':0x6C,
                    'subtract_key':0x6D,
                    'decimal_key':0x6E,
                    'divide_key':0x6F,
                    'F1':0x70,
                    'F2':0x71,
                    'F3':0x72,
                    'F4':0x73,
                    'F5':0x74,
                    'F6':0x75,
                    'F7':0x76,
                    'F8':0x77,
                    'F9':0x78,
                    'F10':0x79,
                    'F11':0x7A,
                    'F12':0x7B,
                    'F13':0x7C,
                    'F14':0x7D,
                    'F15':0x7E,
                    'F16':0x7F,
                    'F17':0x80,
                    'F18':0x81,
                    'F19':0x82,
                    'F20':0x83,
                    'F21':0x84,
                    'F22':0x85,
                    'F23':0x86,
                    'F24':0x87,
                    'num_lock':0x90,
                    'scroll_lock':0x91,
                    'left_shift':0xA0,
                    'right_shift ':0xA1,
                    'left_control':0xA2,
                    'right_control':0xA3,
                    'left_menu':0xA4,
                    'right_menu':0xA5,
                    'browser_back':0xA6,
                    'browser_forward':0xA7,
                    'browser_refresh':0xA8,
                    'browser_stop':0xA9,
                    'browser_search':0xAA,
                    'browser_favorites':0xAB,
                    'browser_start_and_home':0xAC,
                    'volume_mute':0xAD,
                    'volume_Down':0xAE,
                    'volume_up':0xAF,
                    'next_track':0xB0,
                    'previous_track':0xB1,
                    'stop_media':0xB2,
                    'play/pause_media':0xB3,
                    'start_mail':0xB4,
                    'select_media':0xB5,
                    'start_application_1':0xB6,
                    'start_application_2':0xB7,
                    'attn_key':0xF6,
                    'crsel_key':0xF7,
                    'exsel_key':0xF8,
                    'play_key':0xFA,
                    'zoom_key':0xFB,
                    'clear_key':0xFE,
                    '+':0xBB,
                    ',':0xBC,
                    '-':0xBD,
                    '.':0xBE,
                    '/':0xBF,
                    '`':0xC0,
                    ';':0xBA,
                    '[':0xDB,
                    '\\':0xDC,
                    ']':0xDD,
                    "'":0xDE,
                    '`':0xC0}

def press(*args):
    '''
    press, release
    eg press('x', 'y', 'z')
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
            
def pressHoldRelease(*args):
    '''
    press and hold passed in strings. Once held, release
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').
 
    this is useful for issuing shortcut command or shift commands.
    e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
            
    for i in args:
            win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
            time.sleep(.1)
            
while True:
    try:
        f = open('commands.txt')
        lines = f.readlines()
        f.close()
        for line in lines:
            if(line == ""):
                loop = True
            else:
                value_c = (line).split(' ')[1]
                if value_c == "up\n" or value_c == "up":
                    up_c = up_c + 1
                if value_c == "right\n" or value_c == "right":
                    right_c = right_c + 1
                if value_c == "down\n" or value_c == "down":
                    down_c = down_c + 1
                if value_c == "left\n" or value_c == "left":
                    left_c = left_c + 1
                if value_c == "enter\n" or value_c == "enter":
                    enter_c = enter_c + 1
                if value_c == "esc\n" or value_c == "esc":
                    esc_c = esc_c + 1
                if value_c == "space\n" or value_c == "space":
                    space_c = space_c + 1
                if value_c == ".\n" or value_c == ".":
                    stop_c = stop_c + 1
                if value_c == ">\n" or value_c == ">":
                    shiftstop_c = shiftstop_c + 1
                if value_c == "comma/n" or value_c == "comma":
                    comma_c = comma_c + 1
                if value_c == "shiftcomma/n" or value_c == "shiftcomma":
                    shiftcomma_c = shiftcomma_c + 1
                if value_c == "numpad9/n" or value_c == "numpad9":
                    numpad9_c = numpad9_c + 1
                if value_c == "numpad8/n" or value_c == "numpad8":
                    numpad8_c = numpad8_c + 1
                if value_c == "numpad7/n" or value_c == "numpad7":
                    numpad7_c = numpad7_c + 1
                if value_c == "numpad6/n" or value_c == "numpad6":
                    numpad6_c = numpad6_c + 1
                if value_c == "numpad5/n" or value_c == "numpad5":
                    numpad5_c = numpad5_c + 1
                if value_c == "numpad4/n" or value_c == "numpad4":
                    numpad4_c = numpad4_c + 1
                if value_c == "numpad3/n" or value_c == "numpad3":
                    numpad3_c = numpad3_c + 1
                if value_c == "numpad2/n" or value_c == "numpad2":
                    numpad2_c = numpad2_c + 1
                if value_c == "numpad1/n" or value_c == "numpad1":
                    numpad1_c = numpad1_c + 1
                if value_c == "numpad0/n" or value_c == "numpad0":
                    numpad0_c = numpad0_c + 1
                if value_c == "1/n" or value_c == "1":
                    one_c = one_c + 1
                if value_c == "2/n" or value_c == "2":
                    two_c = two_c + 1
                if value_c == "3/n" or value_c == "3":
                    three_c = three_c + 1
                if value_c == "4/n" or value_c == "4":
                    four_c = four_c + 1
                if value_c == "5/n" or value_c == "5":
                    five_c = five_c + 1
                if value_c == "6/n" or value_c == "6":
                    six_c = six_c + 1
                if value_c == "7/n" or value_c == "7":
                    seven_c = seven_c + 1
                if value_c == "8/n" or value_c == "8":
                    eight_c = eight_c + 1
                if value_c == "9/n" or value_c == "9":
                    nine_c = nine_c + 1
                if value_c == "0/n" or value_c == "0":
                    zero_c = zero_c + 1
                if value_c == "backspace/n" or value_c == "backspace":
                    backspace_c = backspace_c + 1
                if value_c == "tab/n" or value_c == "tab":
                    tab_c = tab_c + 1
                if value_c == "shiftup/n" or value_c == "shiftup":
                    shiftup_c = shiftup_c + 1
                if value_c == "altup/n" or value_c == "altup":
                    altup_c = altup_c + 1
                if value_c == "shiftright/n" or value_c == "shiftright":
                    shiftright_c = shiftright_c + 1
                if value_c == "altright/n" or value_c == "altright":
                    altright_c = altright_c + 1
                if value_c == "shiftdown/n" or value_c == "shiftdown":
                    shiftdown_c = shiftdown_c + 1
                if value_c == "altdown/n" or value_c == "altdown":
                    altdown_c = altdown_c + 1
                if value_c == "shiftleft/n" or value_c == "shiftleft":
                    shiftleft_c = shiftleft_c + 1
                if value_c == "altleft/n" or value_c == "altleft":
                    altleft_c = altleft_c + 1
                if value_c == "+/n" or value_c == "+":
                    plus_c = plus_c + 1
                if value_c == "-/n" or value_c == "-":
                    minus_c = minus_c + 1
                if value_c == "*/n" or value_c == "*":
                    asterisk_c = asterisk_c + 1
                if value_c == "\\/n" or value_c == "\\":
                    backslash_c = backslash_c + 1
                if value_c == "|/n" or value_c == "|":
                    shiftbackslash_c = shiftbackslash_c + 1
                if value_c == "//n" or value_c == "/":
                    slash_c = slash_c + 1
                if value_c == "?/n" or value_c == "?":
                    shiftslash_c = shiftslash_c + 1
                if value_c == "[/n" or value_c == "[":
                    leftbracket_c = leftbracket_c + 1
                if value_c == "{/n" or value_c == "{":
                    leftshiftbracket_c = leftshiftbracket_c + 1
                if value_c == "]/n" or value_c == "]":
                    rightbracket_c = rightbracket_c + 1
                if value_c == "}/n" or value_c == "}":
                    rightshiftbracket_c = rightshiftbracket_c + 1
                if value_c == "f1/n" or value_c == "f1":
                    f1_c = f1_c + 1
                if value_c == "f2/n" or value_c == "f2":
                    f2_c = f2_c + 1
                if value_c == "f3/n" or value_c == "f3":
                    f3_c = f3_c + 1
                if value_c == "f4/n" or value_c == "f4":
                    f4_c = f4_c + 1
                if value_c == "f5/n" or value_c == "f5":
                    f5_c = f5_c + 1
                if value_c == "f6/n" or value_c == "f6":
                    f6_c = f6_c + 1
                if value_c == "f7/n" or value_c == "f7":
                    f7_c = f7_c + 1
                if value_c == "f8/n" or value_c == "f8":
                    f8_c = f8_c + 1
                if value_c == "a/n" or value_c == "a":
                    a_c = a_c + 1
                if value_c == "A/n" or value_c == "A":
                    shiftA_c = shiftA_c + 1
                if value_c == "b/n" or value_c == "b":
                    b_c = b_c + 1
                if value_c == "B/n" or value_c == "B":
                    shiftB_c = shiftB_c + 1
                if value_c == "c/n" or value_c == "c":
                    c_c = c_c + 1
                if value_c == "C/n" or value_c == "C":
                    shiftC_c = shiftC_c + 1
                if value_c == "d/n" or value_c == "d":
                    d_c = d_c + 1
                if value_c == "D/n" or value_c == "D":
                    shiftD_c = shiftD_c + 1
                if value_c == "e/n" or value_c == "e":
                    e_c = e_c + 1
                if value_c == "E/n" or value_c == "E":
                    shiftE_c = shiftE_c + 1
                if value_c == "f/n" or value_c == "f":
                    f_c = f_c + 1
                if value_c == "F/n" or value_c == "F":
                    shiftF_c = shiftF_c + 1
                if value_c == "g/n" or value_c == "g":
                    g_c = g_c + 1
                if value_c == "G/n" or value_c == "G":
                    shiftG_c = shiftG_c + 1
                if value_c == "h/n" or value_c == "h":
                    h_c = h_c + 1
                if value_c == "H/n" or value_c == "H":
                    shiftH_c = shiftH_c + 1
                if value_c == "i/n" or value_c == "i":
                    i_c = i_c + 1
                if value_c == "I/n" or value_c == "I":
                    shiftI_c = shiftI_c + 1
                if value_c == "j/n" or value_c == "j":
                    j_c = j_c + 1
                if value_c == "J/n" or value_c == "J":
                    shiftJ_c = shiftJ_c + 1
                if value_c == "k/n" or value_c == "k":
                    k_c = k_c + 1
                if value_c == "K/n" or value_c == "K":
                    shiftK_c = shiftK_c + 1
                if value_c == "l/n" or value_c == "l":
                    l_c = l_c + 1
                if value_c == "L/n" or value_c == "L":
                    shiftL_c = shiftL_c + 1
                if value_c == "m/n" or value_c == "m":
                    m_c = m_c + 1
                if value_c == "M/n" or value_c == "M":
                    shiftM_c = shiftM_c + 1
                if value_c == "n/n" or value_c == "n":
                    n_c = n_c + 1
                if value_c == "N/n" or value_c == "N":
                    shiftN_c = shiftN_c + 1
                if value_c == "o/n" or value_c == "o":
                    o_c = o_c + 1
                if value_c == "O/n" or value_c == "O":
                    shiftO_c = shiftO_c + 1
                if value_c == "p/n" or value_c == "p":
                    p_c = p_c + 1
                if value_c == "P/n" or value_c == "P":
                    shiftP_c = shiftP_c + 1
                if value_c == "q/n" or value_c == "q":
                    q_c = q_c + 1
                if value_c == "Q/n" or value_c == "Q":
                    shiftQ_c = shiftQ_c + 1
                if value_c == "r/n" or value_c == "r":
                    r_c = r_c + 1
                if value_c == "R/n" or value_c == "R":
                    shiftR_c = shiftR_c + 1
                if value_c == "s/n" or value_c == "s":
                    s_c = s_c + 1
                if value_c == "S/n" or value_c == "S":
                    shiftS_c = shiftS_c + 1
                if value_c == "t/n" or value_c == "t":
                    t_c = t_c + 1
                if value_c == "T/n" or value_c == "T":
                    shiftT_c = shiftT_c + 1
                if value_c == "u/n" or value_c == "u":
                    u_c = u_c + 1
                if value_c == "U/n" or value_c == "U":
                    shiftU_c = shiftU_c + 1
                if value_c == "v/n" or value_c == "v":
                    v_c = v_c + 1
                if value_c == "V/n" or value_c == "V":
                    shiftV_c = shiftV_c + 1
                if value_c == "w/n" or value_c == "w":
                    w_c = w_c + 1
                if value_c == "W/n" or value_c == "W":
                    shiftW_c = shiftW_c + 1
                if value_c == "x/n" or value_c == "x":
                    x_c = x_c + 1
                if value_c == "X/n" or value_c == "X":
                    shiftX_c = shiftX_c + 1
                if value_c == "y/n" or value_c == "y":
                    y_c = y_c + 1
                if value_c == "Y/n" or value_c == "Y":
                    shiftY_c = shiftY_c + 1
                if value_c == "z/n" or value_c == "z":
                    z_c = z_c + 1
                if value_c == "Z/n" or value_c == "Z":
                    shiftZ_c = shiftZ_c + 1
        alloutputs = {'up': up_c, 'right': right_c, 'down': down_c, 'left': left_c, 'enter': enter_c, 'esc': esc_c, 'space': space_c, '.': stop_c, '>': shiftstop_c, ',': comma_c, '<': shiftcomma_c, 'npne': numpad9_c, 'npn': numpad8_c, 'npnw': numpad7_c, 'npe': numpad6_c, 'npc': numpad5_c, 'npw': numpad4_c, 'npse': numpad3_c, 'nps': numpad2_c, 'npsw': numpad1_c, 'np0': numpad0_c, '1': one_c, '2': two_c, '3': three_c, '4':four_c, '5': five_c, '6': six_c, '7': seven_c, '8': eight_c, '9': nine_c, '0': zero_c, 'backspace': backspace_c, 'tab': tab_c, 'shiftup': shiftup_c, 'altup': altup_c, 'shiftright': shiftright_c, 'altright': altright_c, 'shiftdown': shiftdown_c, 'altdown': altdown_c, 'shiftleft': shiftleft_c, 'altleft': altleft_c, '+': plus_c, '-': minus_c, '*': asterisk_c, '\\': backslash_c, '|': shiftbackslash_c, '/': slash_c, '?': shiftslash_c, '[': leftbracket_c, '{': leftshiftbracket_c, ']': rightbracket_c, '}': rightshiftbracket_c, 'f1': f1_c, 'f2': f2_c, 'f3': f3_c, 'f4': f4_c, 'f5': f5_c, 'f6': f6_c, 'f7': f7_c, 'f8': f8_c, 'a': a_c, 'A': shiftA_c, 'b': b_c, 'B': shiftB_c, 'c': c_c, 'C':  shiftC_c, 'd': d_c, 'D': shiftD_c, 'e': e_c, 'E': shiftE_c, 'f': f_c, 'F': shiftF_c, 'g': g_c, 'G': shiftG_c, 'h': h_c, 'H': shiftH_c, 'i': i_c, 'I': shiftI_c, 'j': j_c, 'J': shiftJ_c, 'k': k_c, 'K': shiftK_c, 'l': l_c, 'L':shiftL_c, 'm': m_c, 'M': shiftM_c, 'n': n_c, 'N': shiftN_c, 'o': o_c, 'O': shiftO_c, 'p': p_c, 'P': shiftP_c, 'q': q_c, 'Q': shiftQ_c, 'r': r_c, 'R': shiftR_c, 's': s_c, 'S': shiftS_c, 't': t_c, 'T': shiftT_c, 'u': u_c, 'U': shiftU_c, 'v': v_c, 'V': shiftV_c, 'w': w_c, 'W': shiftW_c, 'x': x_c, 'X': shiftX_c, 'y': y_c, 'Y': shiftY_c, 'z': z_c, 'Z': shiftZ_c}
        if(enter_c + esc_c + space_c + stop_c + shiftstop_c + comma_c + shiftcomma_c + numpad9_c + numpad8_c + numpad7_c + numpad6_c + numpad5_c + numpad4_c + numpad3_c + numpad2_c + numpad1_c + numpad0_c+ one_c + two_c + three_c + four_c + five_c + six_c + seven_c + eight_c + nine_c + zero_c + backspace_c + tab_c + up_c + shiftup_c + altup_c + right_c + shiftright_c + altright_c + down_c + shiftdown_c +altdown_c + left_c + shiftleft_c + altleft_c + plus_c + minus_c + asterisk_c + backslash_c + shiftbackslash_c + slash_c + shiftslash_c +leftbracket_c + leftshiftbracket_c + rightbracket_c + rightshiftbracket_c + f1_c + f2_c + f3_c + f4_c + f5_c + f6_c + f7_c +f8_c + a_c + shiftA_c + b_c + shiftB_c + c_c +  shiftC_c + d_c + shiftD_c +  e_c + shiftE_c + f_c + shiftF_c + g_c + shiftG_c + h_c + shiftH_c + i_c + shiftI_c + j_c + shiftJ_c + k_c + shiftK_c + l_c + shiftL_c + m_c + shiftM_c + n_c + shiftN_c + o_c + shiftO_c + p_c + shiftP_c + q_c + shiftQ_c + r_c + shiftR_c + s_c + shiftS_c + t_c + shiftT_c + u_c + shiftU_c + v_c + shiftV_c + w_c + shiftW_c + x_c + shiftX_c + y_c + shiftY_c + z_c + shiftZ_c == 0):
            selected_c = "None"
        else:
            selected_c = max(alloutputs, key = alloutputs.get)
        os.system("cls")
        print("up: " + str(up_c))
        print("right: " + str(right_c))
        print("down: " + str(down_c))
        print("left: " + str(left_c))
        print("a: " + str(a_c))
        print("b: " + str(b_c))
        print("enter: " + str(enter_c))
        print("escape: " + str(esc_c))
        print("space: " + str(space_c))
        print(".: " + str(stop_c))
        print(">: " + str(shiftstop_c))
        print(",: " + str(comma_c))
        print("<: " + str(shiftcomma_c))
        print("npne: " + str(numpad9_c))
        print("npn: " + str(numpad8_c))
        print("npnw: " + str(numpad7_c))
        print("npe: " + str(numpad6_c))
        print("npc: " + str(numpad5_c))
        print("npw: " + str(numpad4_c))
        print("npse: " + str(numpad3_c))
        print("nps: " + str(numpad2_c))
        print("npsw: " + str(numpad1_c))
        print("np0: " + str(numpad0_c))
        print("1: " + str(one_c))
        print("2: " + str(two_c))
        print("3: " + str(three_c))
        print("4: " + str(four_c))
        print("5: " + str(five_c))
        print("6: " + str(six_c))
        print("7: " + str(seven_c))
        print("8: " + str(eight_c))
        print("9: " + str(nine_c))
        print("0: " + str(zero_c))
        print("backspace: " + str(backspace_c))
        print("tab: " + str(tab_c))
        print("shiftup: " + str(shiftup_c))
        print("altup: " + str(altup_c))
        print("shiftright: " + str(shiftright_c))
        print("altright: " + str(altright_c))
        print("shiftdown: " + str(shiftdown_c))
        print("altdown: " + str(altdown_c))
        print("shiftleft: " + str(shiftleft_c))
        print("altleft: " + str(altleft_c))
        print("+: " + str(plus_c))
        print("-: " + str(minus_c))
        print("*: " + str(asterisk_c))
        print("\: " + str(backslash_c))
        print("|: " + str(shiftbackslash_c))
        print("/: " + str(slash_c))
        print("?: " + str(shiftslash_c))
        print("[: " + str(rightbracket_c))
        print("{: " + str(rightshiftbracket_c))
        print("]: " + str(leftbracket_c))
        print("}: " + str(leftshiftbracket_c))
        print("f1: " + str(f1_c))
        print("f2: " + str(f2_c))
        print("f3: " + str(f3_c))
        print("f4: " + str(f4_c))
        print("f5: " + str(f5_c))
        print("f6: " + str(f6_c))
        print("f7: " + str(f7_c))
        print("f8: " + str(f8_c))
        print("a: " + str(a_c))
        print("A: " + str(shiftA_c))
        print("b: " + str(b_c))
        print("B: " + str(shiftB_c))
        print("c: " + str(c_c))
        print("C: " + str(shiftC_c))
        print("d: " + str(d_c))
        print("D: " + str(shiftD_c))
        print("e: " + str(e_c))
        print("E: " + str(shiftE_c))
        print("f: " + str(f_c))
        print("F: " + str(shiftF_c))
        print("g: " + str(g_c))
        print("G: " + str(shiftG_c))
        print("h: " + str(h_c))
        print("H: " + str(shiftH_c))
        print("i: " + str(i_c))
        print("I: " + str(shiftI_c))
        print("j: " + str(j_c))
        print("J: " + str(shiftJ_c))
        print("k: " + str(k_c))
        print("K: " + str(shiftK_c))
        print("l: " + str(l_c))
        print("L: " + str(shiftL_c))
        print("m: " + str(m_c))
        print("M: " + str(shiftM_c))
        print("n: " + str(n_c))
        print("N: " + str(shiftN_c))
        print("o: " + str(o_c))
        print("O: " + str(shiftO_c))
        print("p: " + str(p_c))
        print("P: " + str(shiftP_c))
        print("q: " + str(q_c))
        print("Q: " + str(shiftQ_c))
        print("r: " + str(r_c))
        print("R: " + str(shiftR_c))
        print("s: " + str(s_c))
        print("S: " + str(shiftS_c))
        print("t: " + str(t_c))
        print("T: " + str(shiftT_c))
        print("u: " + str(u_c))
        print("U: " + str(shiftU_c))
        print("v: " + str(v_c))
        print("V: " + str(shiftV_c))
        print("w: " + str(w_c))
        print("W: " + str(shiftW_c))
        print("x: " + str(x_c))
        print("X: " + str(shiftX_c))
        print("y: " + str(y_c))
        print("Y: " + str(shiftY_c))
        print("z: " + str(z_c))
        print("Z: " + str(shiftZ_c))
        print("\nSelected: " + selected_c)
        enter_c = 0
        esc_c = 0
        space_c = 0
        stop_c = 0
        shiftstop_c = 0
        comma_c = 0
        shiftcomma_c = 0
        numpad9_c = 0
        numpad8_c = 0
        numpad7_c = 0
        numpad6_c = 0
        numpad5_c = 0
        numpad4_c = 0
        numpad3_c = 0
        numpad2_c = 0
        numpad1_c = 0
        numpad0_c = 0
        one_c = 0
        two_c = 0
        three_c = 0
        four_c = 0
        five_c = 0
        six_c = 0
        seven_c = 0
        eight_c = 0
        nine_c = 0
        zero_c = 0
        backspace_c = 0
        tab_c = 0
        up_c = 0
        shiftup_c = 0
        altup_c = 0
        right_c = 0
        shiftright_c = 0
        altright_c = 0
        down_c = 0
        shiftdown_c = 0
        altdown_c = 0
        left_c = 0
        shiftleft_c = 0
        altleft_c = 0
        plus_c = 0
        minus_c = 0
        asterisk_c = 0
        backslash_c = 0
        shiftbackslash_c = 0 #|
        slash_c = 0
        shiftslash_c = 0 #?
        leftbracket_c = 0 #[
        leftshiftbracket_c = 0 #{
        rightbracket_c = 0 #]
        rightshiftbracket_c = 0 #}
        f1_c = 0
        f2_c = 0
        f3_c = 0
        f4_c = 0
        f5_c = 0
        f6_c = 0
        f7_c = 0
        f8_c = 0
        a_c = 0
        shiftA_c = 0
        b_c = 0
        shiftB_c = 0
        c_c = 0 
        shiftC_c = 0
        d_c = 0 
        shiftD_c = 0 
        e_c = 0
        shiftE_c = 0
        f_c = 0
        shiftF_c = 0
        g_c = 0
        shiftG_c = 0
        h_c = 0
        shiftH_c = 0
        i_c = 0
        shiftI_c = 0
        j_c = 0
        shiftJ_c = 0
        k_c = 0
        shiftK_c = 0
        l_c = 0
        shiftL_c = 0
        m_c = 0
        shiftM_c = 0
        n_c = 0
        shiftN_c = 0
        o_c = 0
        shiftO_c = 0
        p_c = 0
        shiftP_c = 0
        q_c = 0
        shiftQ_c = 0
        r_c = 0
        shiftR_c = 0
        s_c = 0
        shiftS_c = 0
        t_c = 0
        shiftT_c = 0
        u_c = 0
        shiftU_c = 0
        v_c = 0
        shiftV_c = 0
        w_c = 0
        shiftW_c = 0
        x_c = 0
        shiftX_c = 0
        y_c = 0
        shiftY_c = 0
        z_c = 0
        shiftZ_c = 0
        if selected_c == "up":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('up_arrow')
        if selected_c == "right":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('right_arrow')
        if selected_c == "down":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('down_arrow')
        if selected_c == "left":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('left_arrow')
        if selected_c == "enter":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('enter')
        if selected_c == "backspace":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('backspace')
        if selected_c == "esc":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('esc')
        if selected_c == "space":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('spacebar')
        if selected_c == ".":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press('.')
        if selected_c == ">":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease('shift', '.')
        if selected_c == ",":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press(",")
        if selected_c == "<":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease('left_shift', ',')
        if selected_c == "npne":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_9")
        if selected_c == "npn":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_8")
        if selected_c == "npnw":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_7")
        if selected_c == "npe":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_6")
        if selected_c == "npc":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_5")
        if selected_c == "npw":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_4")
        if selected_c == "npse":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_3")
        if selected_c == "nps":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_2")
        if selected_c == "npsw":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_1")
        if selected_c == "np0":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("numpad_0")
        if selected_c == "1":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("1")
        if selected_c == "2":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("2")
        if selected_c == "3":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("3")
        if selected_c == "4":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("4")
        if selected_c == "5":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("5")
        if selected_c == "6":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("6")
        if selected_c == "7":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("7")
        if selected_c == "8":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("8")
        if selected_c == "9":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("9")
        if selected_c == "0":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("0")
        if selected_c == "backspace":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("backspace")
        if selected_c == "tab":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("tab")
        if selected_c == "shiftup":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", 'up_arrow')
        if selected_c == "altup":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("alt", "up_arrow")
        if selected_c == "shiftright":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "right_arrow")
        if selected_c == "altright":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("alt", "right_arrow")
        if selected_c == "shiftdown":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "down_arrow")
        if selected_c == "altdown":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("alt", "down_arrow")
        if selected_c == "shiftleft":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "left_arrow")
        if selected_c == "altleft":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("alt", "left_arrow")
        if selected_c == "+":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("add_key")
        if selected_c == "-":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("subtract_key")
        if selected_c == "*":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("multiply_key")
        if selected_c == "\\":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("\\")
        if selected_c == "|":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "\\")
        if selected_c == "/":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("divide_key")
        if selected_c == "?":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("left_shift", "/")
        if selected_c == "[":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("[")
        if selected_c == "{":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "[")
        if selected_c == "]":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("]")
        if selected_c == "}":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "]")
        if selected_c == "f1":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F1")
        if selected_c == "f2":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F2")
        if selected_c == "f3":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F3")
        if selected_c == "f4":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F4")
        if selected_c == "f5":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F5")
        if selected_c == "f6":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F6")
        if selected_c == "f7":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F7")
        if selected_c == "f8":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("F8")
        if selected_c == "a":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("a")
        if selected_c == "A":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "a")
        if selected_c == "b":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("b")
        if selected_c == "B":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "b")
        if selected_c == "c":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("c")
        if selected_c == "C":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "c")
        if selected_c == "d":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("d")
        if selected_c == "D":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "d")
        if selected_c == "e":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("e")
        if selected_c == "E":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "e")
        if selected_c == "f":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("f")
        if selected_c == "F":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "f")
        if selected_c == "g":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("g")
        if selected_c == "G":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "g")
        if selected_c == "h":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("h")
        if selected_c == "H":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "h")
        if selected_c == "i":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("i")
        if selected_c == "I":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "i")
        if selected_c == "j":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("j")
        if selected_c == "J":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "j")
        if selected_c == "k":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("k")
        if selected_c == "K":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "k")
        if selected_c == "l":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("l")
        if selected_c == "L":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "l")
        if selected_c == "m":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("m")
        if selected_c == "M":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "m")
        if selected_c == "n":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("n")
        if selected_c == "N":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "n")
        if selected_c == "o":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("o")
        if selected_c == "O":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "o")
        if selected_c == "p":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("p")
        if selected_c == "P":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "p")
        if selected_c == "q":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("q")
        if selected_c == "Q":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "q")
        if selected_c == "r":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("r")
        if selected_c == "R":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "r")
        if selected_c == "s":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("s")
        if selected_c == "S":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "s")
        if selected_c == "t":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("t")
        if selected_c == "T":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "t")
        if selected_c == "u":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("u")
        if selected_c == "U":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "u")
        if selected_c == "v":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("v")
        if selected_c == "V":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "v")
        if selected_c == "w":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("w")
        if selected_c == "W":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "w")
        if selected_c == "x":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("x")
        if selected_c == "X":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "x")
        if selected_c == "y":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("y")
        if selected_c == "Y":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "y")
        if selected_c == "z":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            press("z")
        if selected_c == "Z":
            shell.AppActivate("Dwarf Fortress")
            time.sleep(.01)
            pressHoldRelease("shift", "z")
        with open("commands.txt", "w") as f:
            f.write(' Selected ' + selected_c)
        time.sleep(2)
    except FileNotFoundError:
        loop = True
        
        #WRITE IN ALL KEYS FOR COMMANDS.TXT WRITE LOOP