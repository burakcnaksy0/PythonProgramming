def calculate_pyramid_height(number_of_blocks):
    height = 0
    blocks_used = 0
    
    for level in range(1, number_of_blocks + 1):
        blocks_used += level
        if blocks_used > number_of_blocks:
            break
        height += 1
    return height

if __name__ == "__main__":
    user_blocks = int(input("Enter the number of blocks: "))
    max_height = calculate_pyramid_height(user_blocks)
    print(f"The maximum height of the pyramid is: {max_height}")
