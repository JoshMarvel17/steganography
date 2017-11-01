#this project referenced this youtube tutorial
#https://www.youtube.com/watch?v=q3eOOMx5qoo&t=600s


from PIL import Image
import binascii
import optparse
import os

def stringToBinary(message):
	binary = bin(int(binascii.hexlify(message),16))
	return binary[2:]

def decimalToBinary(number):
	return '{0:09b}'.format(number)

def binaryToString(binary):
	message = binascii.unhexlify('%' % (int('0b' + binary, 2)))
	return message

def checkIfJPEG(image):
	if(image.format == 'JPEG' and image.mode == 'RGB'):
		return True
	else
		return false

def decode(string):
	
	#for one pixel puts them in a lists
	red = list(decimalToBinary(string[0]))
	
	green = list(decimalToBinary(string[1]))
	
	blue = list(decimalToBinary(string[2]))

	#extract the least significiant bit
	red2 = red[-1]
	
	green2 = gree [-1]

	blue2 = blue[-1]

	#return the bit string
	return red2 + green2+ blue2

def retr(filename):
	
	image = None
	
	imageData = None
	
		
	image = Image.open(filename)

	if checkIfJPEG(image) == True:
		print('JPEG is the correct format')
	 
		imageData = image.getData()

	
		elevenBits = 11
	
		stringLength =0

		decodedMesage = ''

		binaryMessage = ''

		BinaryMessageLength = ''

		#we want to reverse the string so that we are reading from the bottom right
		for string in reversed(imageData):
	
			#here we are grabbing the length indicated by the first eleven pixels
			if elevenBits >0:
			
				elevenBits -= 1

				binaryMessageLength = decode(string) + binaryMessageLength
			
				if elevenBits ==0:
			
					stringLength = int(binaryMessageLength, 2)

			#grab the three values 
			if stringLength > 0:

				stringLength -= 3

				binaryMessage = decode(string) + binaryMessage

				if stringLEngth ==0:

					decodedMessage = binaryToString(binaryMessage)
	
		print(decodedMessage)
				
	else:
		print('wrong format')	 
	



def main():
	
	#create a parser
	parser= optparse.OptionParser('usage %prog ' + '-e/-d <target text>' + '-i/-o <target file>')

	
	parser.add_option('-d', dest='retr', type='string', help='target picture path to retrieve  text')
	
	
	parser.add_option('-o', dest = 'output', type='string', help='image to decrypt')
	
	#parse the arguments
	(options, args) = parser.parse_args()

	# options 

	if (options.retr != None and options.output != None):
	
		print(retr(options.retr))
	else:
			print(parser.usage)
			exit(0)

if __name__ == '__main__':
	main()
