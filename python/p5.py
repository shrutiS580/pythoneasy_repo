def prefix(strs):

    result = ""

    for i in range(len(strs[0])):

        ch = strs[0][i]

        for word in strs:

            if i >= len(word) or word[i] != ch:
                return result

        result = result + ch

    return result


strs = input("Enter words separated by space: ").split()

print("Longest Common Prefix:", prefix(strs))