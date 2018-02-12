import os
import sys
import ciphers
import polybius
import affine
import bifid
import transposition

# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome Message
def screen(action):
	if action == "welcome":
		clear_screen();
		print("Hi there! Want to send encrypted messages?\nType quit to exit the program at any time\n\nWe currently have the following ciphers:")	

# Main program
def program():

	# Shows first screen portion
	screen('welcome')

	# Cipher list
	ciphers = ["affine", "bifid", "polybius", "transposition"]

	# Tells the program to stop or continue
	running = True
	# Program Loop
	while running:
		# Showing my ciphers.
		for cipher in ciphers:
			print("-{}".format(cipher.capitalize()))	
		# Asking the user for a cipher option
		user_input = raw_input("\nPlease choose one of the cipher options! Just type in the cipher name: ").lower()

		# Checks if the user input was quit
		if user_input == "quit":
			running = False
		
		# Checks if the choice is a valid cipher
		if user_input in ciphers:
			# Tells Cipher Loop to stop or continue
			cipher_running = True
			# Cipher options
			cipher_options = ["encrypt", "decrypt"]
			# Cipher options loop
			while cipher_running:
				# Asks the user if encrypt or decrypt
				cipher_option = raw_input("Awesome, you chose {}. If you want to change the cipher type: back.\nnow, do you want to encrypt or decrypt?: ".format(user_input.capitalize()))
				# Checks if the user wants to go back
				if cipher_option == "back":
					break
				# Checks if option is quit
				elif cipher_option == "quit":
					# Loop Ends
					running = False
				# Cipher is in options
				else:
					# Checks if user input is a valid option
					if cipher_option in cipher_options:
						
						# Asks the user for the secret message
						secret_message = raw_input("Almost there... What's the secret message you want to {}?: ".format(cipher_option)).lower()

						# Checks for cipher type
						if user_input == "affine":
							# Affine Instance
							ciphy = affine.Affine()
							# Number 1 for key
							number1 = int(raw_input("Please choose a number from 1 to 9: ").lower())
							# Checks if valid number from 1 to 9
							if number1 > 1 and number1 < 9:
								# Asks another number
								number2 = int(raw_input("One more left to go. Please choose another number from 1 to 9: ").lower())
								# Validate numbers
								if number2 > 1 and number2 < 9:
									# Checks for encryption/decryption
									if cipher_option == "encrypt":
										# Encrypt message
										encrypted_message = ciphy.encrypt([number1, number2], secret_message)										
									else:
										# Decrypt message
										encrypted_message = ciphy.encrypt([number1, number2], secret_message)
									# Prints out the secret message
									print("\nAnd here's your secret message, straight from the oven: \n{}\n".format(encrypted_message))
									# Asks user if he/she wants to continue or quit
									user_input2 = raw_input("Do you want to encrypt or decrypt something else? Type yes or no: ").lower()
									# Check if option is quit
									if user_input2 == "quit":
										running = False
										cipher_running = False
									# Check if option is No
									elif user_input2 == "no":
										running = False
										cipher_running = False
									# Check if option is yes
									elif user_input2 == "yes":
										# Clears screen and show menu again
										clear_screen()
										screen("welcome")
										cipher_running = 0
									else:
										print("\nError. Don't worry, just type a valid option: yes or no.\n")
								else:
									print("\nError. Don't worry, just type a valid number from 1 to 9.\n")
							else:
								print("\nError. Don't worry, just type a valid number from 1 to 9.\n")
						elif user_input == "bifid":

							# Creates a Bifid instance
							ciphy = bifid.Bifid()
							# Checks for encryption/decryption
							if cipher_option == "encrypt":
								# Encrypt message
								encrypted_message = ciphy.encrypt(secret_message)
							else:
								# Decrypt message
								encrypted_message = ciphy.decrypt(secret_message)
							# Prints out the secret message
							print("\nAnd here's your secret message, straight from the oven: \n{}\n".format(encrypted_message))
							# Asks user if he/she wants to continue or quit
							user_input2 = raw_input("Do you want to encrypt or decrypt something else? Type yes or no: ").lower()
							# Check if option is quit
							if user_input2 == "quit":
								running = False
								cipher_running = False
							# Check if option is No
							elif user_input2 == "no":
								running = False
								cipher_running = False
							# Check if option is yes
							elif user_input2 == "yes":
								# Clears screen and show menu again
								clear_screen()
								screen("welcome")
								cipher_running = 0
							else:
								print("\nError. Don't worry, just type a valid option: yes or no.\n")
						elif user_input == "polybius":

							# creates a polybius instance
							ciphy = polybius.Polybius()
							# Checks for encryption/decryption
							if cipher_option == "encrypt":
								# Encrypt message
								encrypted_message = ciphy.encrypt(secret_message)
							else:
								# Decrypt message
								encrypted_message = ciphy.decrypt(secret_message)
							# Prints out the secret message
							print("\nAnd here's your secret message, straight from the oven: \n{}\n".format(encrypted_message))
							# Asks user if he/she wants to continue or quit
							user_input2 = raw_input("Do you want to encrypt or decrypt something else? Type yes or no: ").lower()
							# Check if option is quit
							if user_input2 == "quit":
								running = False
								cipher_running = False
							# Check if option is No
							elif user_input2 == "no":
								running = False
								cipher_running = False
							# Check if option is yes
							elif user_input2 == "yes":
								# Clears screen and show menu again
								clear_screen()
								screen("welcome")
								cipher_running = 0
							else:
								print("\nError. Don't worry, just type a valid option: yes or no.\n")
						else:

							# Creates a Transposition instance
							ciphy = polybius.Transposition()
							# Checks for encryption/decryption
							if cipher_option == "encrypt":
								# Encrypt message
								encrypted_message = ciphy.encrypt(secret_message)
							else:
								# Decrypt message
								encrypted_message = ciphy.decrypt(secret_message)
							# Prints out the secret message
							print("\nAnd here's your secret message, straight from the oven: \n{}\n".format(encrypted_message))
							# Asks user if he/she wants to continue or quit
							user_input2 = raw_input("Do you want to encrypt or decrypt something else? Type yes or no: ").lower()
							# Check if option is quit
							if user_input2 == "quit":
								running = False
								cipher_running = False
							# Check if option is No
							elif user_input2 == "no":
								running = False
								cipher_running = False
							# Check if option is yes
							elif user_input2 == "yes":
								# Clears screen and show menu again
								clear_screen()
								screen("welcome")
								cipher_running = 0
							else:
								print("\nError. Don't worry, just type a valid option: yes or no.\n")
					else:
						# Tells the user to input a correct choice.
						print("\nError. Don't worry, just type a valid option.\n")

		else:
			# Tells the user to input a correct choice.
			print("\nError. Don't worry, just type a valid option.\n")				

# Main Code
if __name__ == "__main__":
		
	# Runs the program
	program()



