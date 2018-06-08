counter = -1    # -1 so it starts at 0, the first line

with open('out2.txt', 'r') as file:
    data = file.read().splitlines()    # reads lines without annoying spaces

print("The first line is: ", data[counter + 1])    # kick-off
choice = input("(A)pprove, (T)rim, or e(X)it... ")

while choice.upper() != 'X':
    if choice.upper() == 'A':
        counter = counter + 1
    elif choice.upper() == 'T':
        counter = counter + 1
        with open("trims.txt", 'a') as f1:    # copies string to f1.txt
            f1.write(data[counter])
            f1.write("\n")

# doesn't work this way (see desc for options):
#        infile = open('out2.txt', 'r').readlines()
#        with open('approved.txt', 'a') as outfile:
#            for index,line in enumerate(infile):
#                if index != counter:
#                    outfile.write(line)

    print("Next line is: ", data[counter + 1])
    choice = input("(A)pprove, (T)rim, or e(X)it... ")
