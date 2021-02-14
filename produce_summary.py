
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


print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()

day_1 = produce_summary("um-deliveries-20140519.txt")

print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()

day_2 = produce_summary("um-deliveries-20140520.txt")


print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()

day_3 = produce_summary("um-deliveries-20140521.txt")
