import random
import string

def get_length() -> int:
	length = input("Length: ")
	try:
		length = int(length)
		if length > 0:
			return length

		#once u throw an exception it will auto look for an except, if it cant find any it will crash (in this case we put a generic exception )
		raise Exception("The length provided needs to be greater than zero.")
		#raise Exception("test")
	except ValueError:
		print("{} is not a number, please try again.".format(length))
		get_length()
	except Exception as e:
		print(e)
		get_length()
	except:
		print("{} is not a valid input".format(length))
		get_length()

def generate_password(length: int) -> str:
	return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
	
def generate_new_pw():
	new_password = input("Would you like a new password? ").lower()
	if new_password == 'y':
		return True

	return False

if __name__ == '__main__':
	while True:
		length = get_length()
		print(generate_password(length))
		if generate_new_pw() == False:
			break