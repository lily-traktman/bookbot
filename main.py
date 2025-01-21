def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    length = wordcount(file_contents)
    chars=charcount(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{length} words found in the document \n")
    
 
    for char in chars:
        print(f"The '{char}' character was found {chars[char]} times")      


def wordcount(text):
    split = text.split()
    return len(split)

def charcount(text):
    textarr = list(text.lower())
    chars = {}
    for char in textarr:
        if char in list("abcdefghijklmnopqrstuvwxyz"):
            try:
                chars[char] = chars[char]+1
            except:
                chars[char] =1
    return chars


if __name__ == "__main__":
    main()