def longest_happy_prefix(s):
    n = len(s)
    lps = [0] * n
    j = 0

    for i in range(1, n):
        while (j > 0 and s[i] != s[j]):
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0

    length_of_happy_prefix = lps[-1]
    return s[:length_of_happy_prefix]

def main():
    s = input().strip()
    print(longest_happy_prefix(s))

if __name__ == "__main__":
    main()
