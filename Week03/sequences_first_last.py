def remove_duplicates(seq: list) -> list:
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def list_counts(seq: list) -> dict:  
    count_dict = {}
    for item in seq:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

def reverse_dict(seq: dict) -> dict:  
    result = {}
    for key, value in seq.items():
        if value in result:
            result[value] = key
        else:
            result[value] = key
    return result

if __name__ == "__main__":
    input_list = [1, 2, 2, 3, 3, 3, 4]
    print("Original list:", input_list)

    print("*" * 30)
    no_duplicates = remove_duplicates(input_list)
    print("List after removing duplicates:", no_duplicates)

    count_result = list_counts(input_list)
    print("Count of each element in the list:", count_result)

    reversed_dict = reverse_dict(count_result)
    print("Reversed dictionary:", reversed_dict)
    print("*" * 30)
