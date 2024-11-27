path_to_file = 'books/frankenstein.txt'
def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        no_of_words = count_words(file_contents)        
        char_count = count_characters(file_contents)
        char_count = {k: v for k, v in sorted(char_count.items(), reverse=True, key=lambda item: item[1])}
        
        print(f'--- Begin report of {path_to_file} ---')
        print(f'{no_of_words} words found in the document\n\n')
        for char, freq in char_count.items():
            if char != ' ':
                print(f"The '{char}' character was found {freq} times")
                
        print(f'--- End report ---')
                
def count_words(file_contents):
    string = file_contents.split()

    return len(string)

def count_characters(file_contents):
    string = file_contents.lower()
    frequency = dict()
    for char in string:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            if char in frequency:
                frequency[char] += 1
            else:
                frequency.update({char: 1})
    
    return frequency

def sort_on(d):
    return d
        
main()