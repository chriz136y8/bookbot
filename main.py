def report(num,dictionary,filename):
    report = f"--- Begin report of {filename} ---\n"
    sorted_d = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    report += f"{num} words found in the document \n\n"
    keys = sorted_d.keys()

    for char in keys:
        if char.isalpha():
            number = sorted_d[char]
            report += f"The '{char}' character was found {number} times.\n"
    report += "--- End report ---"
    return report


def char_frequency(text):
    lowered_string = text.lower()
    frequency = {}

    for i in lowered_string:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

def count_words(text) :
    words = text.split()
    count = len(words)
    return count


def main():
    filename = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    num_words =count_words(file_contents)
    freq_dictionary = char_frequency(file_contents)
    print(report(num_words,freq_dictionary,filename))
    
    
    

if __name__ == '__main__':
    main()