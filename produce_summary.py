
def produce_summary(filename):                  #def function to take in file for each day

    file = open(filename)                   #open the file
    for line in file:                       #loop through each line
        line = line.rstrip()                #remove whitespace
        words = line.split('|')             #Split into sections wherever there's a '|'

        melon = words[0]                    #first section is the melon
        count = words[1]                    #Second section gives the count
        amount = words[2]                   #3rd section gives amount

        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))              #print the totals


print("Day 1")                              #call function on day 1 file
day_1 = produce_summary("um-deliveries-20140519.txt")

print("Day 2")                              #call function on day 2 file
day_2 = produce_summary("um-deliveries-20140520.txt")

print("Day 3")                              #call function on day 3 file
day_3 = produce_summary("um-deliveries-20140521.txt")
