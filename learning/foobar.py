from pprint import pprint


def main():
    book = "aaaaaaaaaaaaaaaaaaaaaaaaaThe foo aaaaaaaaaaa aaa quick brown fox jumps foobar aaaaaaaaaa bar over the foobaaaaa lazy dog foobar"
    word = "aaa"
    combined_word_and_book = word + "^" + book + "$"

    longest_match_arr = {}

    for idx, _ in enumerate(combined_word_and_book):
        suffix = combined_word_and_book[idx + 1 :]
        for jdx, _ in enumerate(suffix):
            if suffix[jdx] != combined_word_and_book[jdx]:
                break
        if jdx:
            longest_match_arr[idx] = (suffix[:-1], jdx)
    pprint(longest_match_arr)


def is_it_easy():
    book = "aabb"
    word = "ab"
    book_length, word_length = len(book), len(word)
    bhash = hash(book)
    whash = hash(word)
    if book_length < word_length:
        return None
    elif book_length == word_length:
        return book == word
    for idx in range(0, book_length + 1):
        slice_word = book[idx : idx + word_length]
        if whash == bhash:
            if slice_word == book[idx : idx + word_length]:
                return idx
        whash = hash(slice_word)
    return None


def asterisk(string: str):
    password_start = string[0]

    matches_idx = []

    for idx, chr in enumerate(string[1:], start=1):
        if chr == password_start:
            matches_idx.append(idx)

    password_continues = True

    idx = 1

    # while idx < len(string):
    next_chr = string[idx]

    for _match_idx in range(len(matches_idx)):
        if string[idx + matches_idx[_match_idx]] == next_chr:
            matches_idx[_match_idx] = idx
        else:
            break

    print(matches_idx)

    return matches_idx


def stupid_asterisk(string: str) -> None:
    substring_length = 1

    best_match = "Just a legend"
    len_string = len(string)

    while substring_length < len_string:
        start = string[:substring_length]
        if start == string[len_string - substring_length :] and string[1:-1].count(
            start
        ):
            best_match = start
        substring_length += 1
    return best_match


def z(string, idx):
    if not idx:
        return 0
    counter = 0
    for a, b in zip(string, string[idx:]):
        if a == b:
            counter += 1
        else:
            break
    return counter


def find_substring(s):
    n = len(s)

    # Check for a palindrome
    if s == s[::-1]:
        return s

    max_length = 0
    max_idx = 0

    # Using the z-function to find the longest prefix-suffix
    for i in range(1, n):
        length = z(s, i)
        if i + length == n and length > max_length:
            max_length = length
            max_idx = i

    if max_length > 0:
        return s[max_idx : max_idx + max_length]
    else:
        return "Just a legend"


def compute_lps(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def efficient_asterisk(string):
    n = len(string)
    lps = compute_lps(string)

    print(lps)

    if lps[-1] == 0:
        return "Just a legend"

    match_length = lps[-1]

    if match_length <= n // 2:
        return string[:match_length]
    else:
        return "Just a legend"


print(efficient_asterisk("fixprefixsuffix"))
print(efficient_asterisk("abcdabc"))
print(efficient_asterisk("qwertyqwertyqwerty"))
print(efficient_asterisk("aaaaaaaaaa"))
