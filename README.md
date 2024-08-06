# String Algorithms

This repository contains two string manipulation algorithms implemented in Python:

1. `mergeAlternately`: Merges two strings by alternating characters from each string.
2. `gcdOfStrings`: Finds the greatest common divisor (GCD) of two strings, defined as the largest string that can divide both strings.

## Algorithms

### 1. mergeAlternately

This function takes two strings and merges them by alternating characters from each string.

#### Function Signature

```python
def mergeAlternately(word1: str, word2: str) -> str:

## Kids With the Greatest Number of Candies

### Problem Statement:
There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i-th` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `True` if, after giving the `i-th` kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or `False` otherwise.

### Solution:
See `solutions.py` for the solution.

## Can Place Flowers

### Problem Statement:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer `n`, return `True` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and `False` otherwise.

### Solution:
See `solutions.py` for the solution.

## Running Tests

To run the tests, execute the `solutions.py` file. It contains test cases for both problems.