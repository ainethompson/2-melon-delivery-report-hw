
def produce_summary(day_num, filename):     #def function to take in file for each day

    print("Day", day_number)
    file = open(filename)                   #open the file

    for line in file:                       #loop through each line
        line = line.rstrip()                #remove whitespace
        words = line.split('|')             #Split into sections wherever there's a '|'

        melon = words[0]                    #first section is the melon
        count = words[1]                    #Second section gives the count
        amount = words[2]                   #3rd section gives amount

        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))              #print the totals

    file.close()

                                           #call function on day 1 file
produce_summary(1, "um-deliveries-20140519.txt")

produce_summary(2, "um-deliveries-20140520.txt")

produce_summary(3, "um-deliveries-20140521.txt")
