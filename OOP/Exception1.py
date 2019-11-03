# import time
#
# class ShortInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# class LongInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# class BadWordException(Exception):
#     def __init__(self, badword):
#         Exception.__init__(self)
#         self.badword = badword
#
# class numberException(Exception):
#     def __init__(self, number):
#         Exception.__init__(self)
#         self.number = number
#
# class symbolException(Exception):
#     def __init__(self, symbol):
#         Exception.__init__(self)
#         self.symbol = symbol
# badwords = ('fuck', 'bitch', 'cyka', 'naxui')
# numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
# symbols = ('!', '@', '#', '$', '%', '^', '&', '*', ';', '?')
#
# try :
#     text = input("Enter a string : ").strip(' ')
#     if len(text) < 5:
#         raise ShortInputException(len(text), 5)
#     if len(text) > 10:
#         raise LongInputException(len(text), 10)
#     for badword in badwords:
#         if text.lower().find(badword) != -1:
#             raise BadWordException(badword)
#     for number in numbers:
#         if text.lower().find(number) != -1:
#             raise numberException(number)
#     for symbol in symbols:
#         if text.lower().find(symbol) != -1:
#             raise symbolException(symbol)
# except BadWordException as ex:
#     print("BadWordException: You have used a badword : {} ".format(ex.badword))
# except ShortInputException as ex:
#     print("ShortInputException: Your entered string was too small. Should be atleast {}".format(ex.atleast))
# except LongInputException as ex:
#     print("LongInputException: Your entered string was too much. Should be atleast {}".format(ex.atleast))
# except numberException as ex:
#     print("NumberException: You have used the number {}".format(ex.number))
# except symbolException as ex:
#     print("SymbolException: You have used the symbol '{}'".format(ex.symbol))
#
#
# time.sleep(5)
# input("Press any key to exit...")
import sys
import time

f = None
try:
    f = open("poem.txt")
    #Our ususal file-reading idiom

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        #To make sure it run for a while

        time.sleep(2)

except IOError:
        print("Could not find file poem.txt")

except KeyboardInterrupt:
        print("!! You cancelled the reading from the file.")

finally:
    if f:
        f.close()
    print("(Cleaning up : Closed the File)")