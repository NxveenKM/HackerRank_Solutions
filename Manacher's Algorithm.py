def longest_palindromic_substring(s):
    if not s:
        return ""

    max_length = 0
    start = 0

    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_length:
                max_length = right - left + 1
                start = left
            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_length:
                max_length = right - left + 1
                start = left
            left -= 1
            right += 1

    return s[start:start + max_length]

def main():
    s = input().strip()
    print(longest_palindromic_substring(s))

if __name__ == "__main__":
    main()
