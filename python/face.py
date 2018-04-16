# draws a face using ASCII Characters
a= ("_"* 6)
# variables
hair = "\t" + "|" * 20
chin =  "\t" + "______" + "\t" + "______"
eyes = "\t|" + " " * 18 + "|\n"
eyes = eyes * 2
eyes = eyes + "\t|" + " " * 5 + "o" + " " * 6 + "o" + " " * 5 + "|"
ears =  " " * 7 + "_|" + " " * 18 + "|_\n"
ears = ears + ' ' * 6 + "|_" + ' ' * 20 + '_|'
mouth = "\t" + "|" + ' ' * 3 + '|__________|' + ' ' * 3 + "|\n"
mouth = mouth + '\t|' + ' '* 18 + '|'


# output
print hair
print eyes
print ears
print mouth
print chin
print "\t" + "as" + "\t"+"ada"
#print
