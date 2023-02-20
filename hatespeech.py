from difflib import SequenceMatcher

with open("1.txt") as file1, open("2.txt") as file2:
    filldata=file1.read()
    file2data=file2.read()
    similarity=SequenceMatcher(None, filldata, file2data).ratio()
    print(similarity*100)

    if similarity > 0:
        print("Hate speech detected")
    else:
        print("None Detected")
