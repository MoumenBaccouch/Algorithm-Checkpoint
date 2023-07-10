def count_words_and_vowels(sentence):
  """Counts the number of words and vowels in a sentence.

  Args:
    sentence: A string.

  Returns:
    A tuple of the number of words, the number of vowels, and the sentence.
  """

  words = 0
  vowels = 0
  for char in sentence:
    if char == " ":
      words += 1
    elif char in "aeiouAEIOU":
      vowels += 1
  return words, vowels, sentence


def main():
  sentence = "This is a sentence."
  words, vowels, sentence = count_words_and_vowels(sentence)
  print("The sentence has {} words and {} vowels.".format(words, vowels))


if __name__ == "__main__":
  main()
