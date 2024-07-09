letters = ["Q", "S", "A", "M", "Z", "R"]
for i in range(len(letters)):
    for j in range(0, (len(letters)-i)-1):
        if letters[j] > letters[j+1]:
            letters[j], letters[j+1] = letters[j+1], letters[j]
            print("Sort", letters)