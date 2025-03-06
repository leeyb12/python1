import re

def count_words(text):
    words = re.findall(r'[가-힣a-zA-Z0-9]+', text)
    return len(words)

def count_characters(textr, include_spaces=True):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace("  ", ""))

def main():
    text = input("텍스트를 입력하세요: ")
    word_count = count_words(text)
    char_count_with_spaces = count_characters(text, include_spaces = True)
    char_count_without_spaces = count_characters(text, include_spaces=False)

    print(f"단어 수: {word_count}")
    print(f"공백 포함 글자 수: {char_count_with_spaces}")
    print(f"공백 제외 글자 수: {char_count_without_spaces}")

    if __name__=="__main__":
        main()