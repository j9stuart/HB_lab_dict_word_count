# put your code here.

# define function:

# create empty dictionary
# open file

# for each line in the file:
#   strip line (type string) of white space
#   split lines of text by space, creating a list

#   for each word in list:
    #(fancy)  see if the value of key is in dictionary, if not, add 1 to value 0
    
    #(not fancy) if key exists in dict:
    #               add 1 to its value for that key
    #            otherwise, 
    #               make a new key
    #               set value to 1
    # return dictionary

# close file

# call function

def word_count(testfile):
    word_dict = {}
    test_file = open(testfile)

    for line in test_file:
        line = line.rstrip()
        split_line = line.split(" ")
       
        for word in split_line:
            # word_dict[word] = word_dict.get(word, 0) + 1
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    test_file.close()
    return word_dict

word_count_dict = word_count("test.txt")

def clean_word_count(word_count_dict1):
    for word, count in word_count_dict.items():
        print "{} {}".format(word, count)

print clean_word_count(word_count_dict)

