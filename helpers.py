
def add_list_to_all_items_in_dict(dict1, list1):
  """Adds a list to all items in a dictionary.

  Args:
    dict1: The dictionary to add the list to.
    list1: The list to add to all items in the dictionary.

  Returns:
    A new dictionary with the list added to all items.
  """

  new_dict = {}
  for key, value in dict1.items():
    new_dict[key] = value + list1
  return new_dict