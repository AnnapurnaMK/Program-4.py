from typing import List, Dict

def count_multiples(data: List[int]) -> Dict[int, int]:
    """
    Counts how many numbers in the input list are divisible by each number from 1 to 9.

    Parameters:
    ----------
    data : List[int]
        A list of integers to analyze.

    Returns:
    -------
    Dict[int, int]
        A dictionary with keys from 1 to 9 and values representing counts of divisible numbers.
    """
    return {i: sum(1 for num in data if num % i == 0) for i in range(1, 10)}

def main():
    # Example input
    input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    
    result = count_multiples(input_list)
    
    print("Output:")
    print(result)

if __name__ == "__main__":
    main()
