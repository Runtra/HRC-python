from boxClass import box

def main():
	try:
		c = box({500:6, 300:7, 2:4})
	except Exception as e:
		print(e, end="\n\n")

	try:
		c = box({500:6, 100:7, 2:4})
		print(str(c), end="\n\n")

		try:
			c.add({250:2})
		except Exception as e:
			print(e, end="\n\n")

		try:
			c.add({50:2, 2:1})
			print()
			print(str(c), end="\n\n")

			try:
				c.substract({50:3, 100:1})
			except Exception as e:
				print(e, end="\n\n")
			
			c.substract({50:2, 100:1})
			print()
			print(str(c))

		except Exception as e:
			print(e, end="\n\n")

	except Exception as e:
		print(e, end="\n\n")

if __name__ == '__main__':
	main()