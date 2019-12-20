'''
*** Wordlist Generator Fedora Project - Simon ***

These are the rules being applied (based on research regarding effective rules):

- Append 0...9
- Append 0...9 0...9
- Append 0...9 0...9 0...9
	= append_numbers()

- Uppercase
- Title case
	= modify_case()

- Substitute 'a' with '@'
	= sub_A()

- 1337 mode (Hello -> h3ll0)
	= convert_leet()
'''

import string

words = []


def main():
    get_input()
    append_numbers()
    modify_case()
    sub_A()
    convert_leet()
    print "Wordlist created (wordlist.txt)"

def get_input():
    num_inputs = int(raw_input("How many words would you like to input for the wordlist generation?: "))
    for i in range(num_inputs):
	input_word = raw_input("[{}] Enter a word: ".format(i+1))
	words.append(input_word.lower())

def append_numbers():
    with open("wordlist.txt", "w") as wordlist:
	wordlist.write('\n'.join(words) + '\n')
	for i in range(10):
	    wordlist.write('\n'.join([s + str(i) for s in words]) + '\n')
	    for j in range(10):
	 	wordlist.write('\n'.join([s + str(i) + str(j) for s in words]) + '\n')
 		for k in range(10):
		    wordlist.write('\n'.join([s + str(i) + str(j) + str(k) for s in words]) + '\n')

def modify_case():
    with open("wordlist.txt", "a+") as wordlist:
	wordlist.write(''.join([''.join([z.upper(), z.title()]) for z in wordlist]))

def sub_A():
    with open("wordlist.txt", "a+") as wordlist:
	replacements = ''.join([s.replace('a', '@') for s in wordlist]).strip('\n')
	for x in replacements:
	    if x not in wordlist.read():
		wordlist.write(x)

def convert_leet():
    leet_dict = {'a':'4', 'b':'6', 'c':'(', 'e':'3', 'g':'9', 'i':'!', 'l':'1', 'o':'0', 's':'5', 't':'7'}
    trans = string.maketrans('abcegilost', '46(39!1057')    
    with open("wordlist.txt", "a+") as wordlist:
	replacements = ''.join([s.translate(trans) for s in wordlist]).strip('\n')
	for x in replacements:
	    if x not in wordlist.read():
		wordlist.write(x)

main()
