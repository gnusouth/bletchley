"""Useful tools for solving substitution ciphers"""

import random

lc_letters = [chr(ord("a") + i) for i in range(26)]
uc_letters = [chr(ord("A") + i) for i in range(26)]
letters = [l for l in lc_letters]
letters.extend(uc_letters)

def caesar(text, shift=0):
	"Perform a Caesar shift on a given piece of text"
	shifted = ""
	for c in text:
		if c not in letters:
			shifted += c
			continue
		elif c.isupper():
			C = ord(c) - ord("A") + shift
			C = (C % 26) + ord("a")
		elif c.islower():		
			C = ord(c) - ord("a") + shift
			C = (C % 26) + ord("A")
		C = chr(C)
		shifted += C
	return shifted

def mono(text, key):
	"Substitute each letter from the text with a match from the key"
	output = ""
	for c in text:
		if c in key:
			output += key[c]
		else:
			output += c	
	return output

def random_alphabet():
	"Generate a random key"
	shuffled = [i for i in range(26)]
	for i in shuffled:
		j = random.randint(0, 25)
		temp = shuffled[i]
		shuffled[i] = shuffled[j]
		shuffled[j] = temp
	key = {uc_letters[i]: lc_letters[shuffled[i]] for i in shuffled}
	return key

def find_repeats(string, l=3):
	"Find the repeated words of length l in a given string"
	words = {}
	n = len(string)
	for i in range(0, n - l + 1):
		w = string[i:i + l]
		if w in words:
			words[w] += 1
		else:
			words[w] = 1

	repeats = {}
	for w in words:
		if words[w] > 1:
			repeats[w] = words[w]

	return repeats

def freq(ciphertext):
	"Count the frequency of each letter in the ciphertext"
	freq = {l: 0 for l in uc_letters}
	n = 0
	for c in ciphertext:
		if c in uc_letters:
			freq[c] += 1
			n += 1

	for l in freq:
		freq[l] = round(freq[l]/n, 3)
	return freq
