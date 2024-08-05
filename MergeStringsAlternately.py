# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    # result = []
    # i = 0
    # while i < len(word1) or i < len(word2):
    #     if i < len(word1):
    #         result.append(word1[i])
    #     if i < len(word2):
    #         result.append(word2[i])
    #     i += i
    # return ''.join(result)

    # return result
    str = ""
    count = 0
    while count < min(len(word1), len(word2)):
        str += word1[count]
        str += word2[count]

        count += 1
    return str + word1[count:] + word2[count:]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(mergeAlternately(word1='abc', word2='pqr'))
    print(mergeAlternately(word1='ab', word2='pqrs'))
    print(mergeAlternately(word1='abcd', word2='pq'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
