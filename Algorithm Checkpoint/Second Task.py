def sum_of_distinct_elements(set1, set2):
  """Computes the sum of all distinct elements from two sets.

  Args:
    set1: A list of elements.
    set2: A list of elements.

  Returns:
    The sum of all distinct elements from two sets.
  """

  sum = 0
  distinct_elements = set()
  for element in set1:
    if element not in distinct_elements:
      sum += element
      distinct_elements.add(element)
  for element in set2:
    if element not in distinct_elements:
      sum += element
      distinct_elements.add(element)
  return sum


def main():
  set1 = [3, 1, 7, 9]
  set2 = [2, 4, 1, 9, 3]
  sum = sum_of_distinct_elements(set1, set2)
  print("The sum of distinct elements is {}".format(sum))


if __name__ == "__main__":
  main()
