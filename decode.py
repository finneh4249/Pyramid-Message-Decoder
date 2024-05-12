import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: python decode.py <message_file>")
        return 1
    message_file = argv[1]
    decodedMsg = decode(message_file)
    if decodedMsg == None:
        return 1
    return 0
    
def decode(message_file):
    message_dict = createDict(message_file)
    if not message_dict:
        print("File is empty")
        return None
    pyramid = createPyramid(message_dict)
    if not pyramid:
        print("Invalid pyramid")
        return None
    decodedMsg = decodeMsg(pyramid)
    print(decodedMsg)
    return decodedMsg
         
                   
def decodeMsg(pyramid):
    message = ""
    for row in pyramid:
        message += row[-1] + " "
    return message
          
          
def createPyramid(dict):
    pyramid = [] 
    counter = 1
    nextKey = 1
    while dict:
        row = []
        for i in range(counter):
            if nextKey in dict:
                row.append(dict.pop(nextKey))
                nextKey+=1
            else:
                return None
        pyramid.append(row)
        counter+=1
    return pyramid
           
            
def createDict(file):
    message_dict = {}
    print("CreateDict called with file:", file)

    if not file:
        print("File is null")
        return None

    try:
        with open(file, 'r') as file_obj:
            print("Opened file successfully")
            for line in file_obj:
                line = line.strip()
                if not line:
                    continue
                number, word = line.split(' ', 1)
                try:
                    number = int(number)
                except ValueError:
                    print("Invalid number:", number)
                    continue
                message_dict[number] = word
                print("Added", number, "=>", word, "to message_dict")
    except FileNotFoundError:
        print("File not found:", file)
        return None

    return message_dict







if __name__ == "__main__":
    sys.exit(main(sys.argv))



