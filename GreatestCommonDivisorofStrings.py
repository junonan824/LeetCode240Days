def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    from math import gcd
    return str1[:gcd(len(str1), len(str2))]


if __name__ == '__main__':
    print(gcdOfStrings("ABCABC", "ABC"))
    print(gcdOfStrings("ABABAB", "ABAB"))
    print(gcdOfStrings("LEET", "CODE"))
