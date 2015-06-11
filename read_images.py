data_dict = {}
data_list = []

def createDictionaryModified(filename):
    path = "/Users/emisshula/Documents/julie/smile"
    basename = "smile_items.json"
    filename = path + "/" + basename
    file = open(filename)
    contents = file.read()
    lines = contents.split("\n")
    for line in lines:
        imageURL = lines[0].split(',')[0].split('"')[3]
        data_list.append(imageURL)
    file.close()
    
      



