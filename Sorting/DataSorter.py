import pandas as pd
import re

#Sorting Algorithms For One Column Sorting 
def bubble_sort(data, column):
        print(f"Bubble Sort is running on column: {column}")

        # Bubble Sort algorithm
        def bubble_sort_recursive(arr):
            n = len(arr)
            for i in range(n):
                # Track if there was any swap in the current pass
                swapped = False
                for j in range(0, n-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                        swapped = True
                if not swapped:
                    break
        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]

        if valid_values:
            # Extract only the values for sorting
            array_to_sort = [value[0] for value in valid_values]
            bubble_sort_recursive(array_to_sort)
            sorted_array = sorted(valid_values, key=lambda x: x[0])
            formatted_sorted_prices = [item[1] for item in sorted_array]
            for index, invalid in invalid_values_with_index:
                formatted_sorted_prices.insert(index, invalid)
            return column, formatted_sorted_prices     
            
        else:
            return [item[1] for item in invalid_values_with_index]

def insertion_sort(data, column):
        print(f"Insertion Sort is running on column: {column}")

        # Main function to perform insertion sort
        def insertion_sort_algorithm(arr):
            # Traverse through 1 to len(arr)
            for i in range(1, len(arr)):
                key = arr[i]  # The element to be positioned
                j = i - 1
                while j >= 0 and compareforheap(key, arr[j]):
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        # Clean and extract data from the specified column
        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]

        if valid_values:
            # Extract only the values for sorting
            array_to_sort = [value[0] for value in valid_values]

            # Sort the array using Insertion Sort
            insertion_sort_algorithm(array_to_sort)
            sorted_array = sorted(valid_values, key=lambda x: x[0])
            formatted_sorted_prices = [item[1] for item in sorted_array]
            for index, invalid in invalid_values_with_index:
                formatted_sorted_prices.insert(index, invalid)
            return column, formatted_sorted_prices 
        else:
            return [item[1] for item in invalid_values_with_index]


def selection_sort(data, column):
        print(f"Selection Sort is running on column: {column}")

        # Selection Sort algorithm
        def selection_sort_recursive(arr):
            n = len(arr)
            for i in range(n):
                min_index = i
                for j in range(i+1, n):
                    if arr[j] < arr[min_index]:
                        min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]
        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]

        if valid_values:
            # Extract only the values for sorting
            array_to_sort = [value[0] for value in valid_values]
            selection_sort_recursive(array_to_sort)
            sorted_array = sorted(valid_values, key=lambda x: x[0])
            formatted_sorted_prices = [item[1] for item in sorted_array]
            for index, invalid in invalid_values_with_index:
                formatted_sorted_prices.insert(index, invalid)
            return column, formatted_sorted_prices 
        else:
            return [item[1] for item in invalid_values_with_index]

def merge_sort(data, column):
        print(f"Merge Sort is running on column: {column}")
        def merge_sort_recursive(arr):
            if len(arr) > 1:
                mid = len(arr) // 2  # Finding the mid of the array
                left_half = arr[:mid]  # Dividing the elements into two halves
                right_half = arr[mid:]
                merge_sort_recursive(left_half)
                merge_sort_recursive(right_half)

                i = j = k = 0

                # Merging the sorted halves
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                # Checking if any element was left in left_half
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]

        if valid_values:
            array_to_sort = [value[0] for value in valid_values]
            merge_sort_recursive(array_to_sort)
            sorted_array = sorted(valid_values, key=lambda x: x[0])
            formatted_sorted_prices = [item[1] for item in sorted_array]
            for index, invalid in invalid_values_with_index:
                formatted_sorted_prices.insert(index, invalid)

            return column, formatted_sorted_prices 
        else:
            return [item[1] for item in invalid_values_with_index]

def quick_sort(data, column):
        print(f"Quick Sort is running on column: {column}")

        # Function to partition the array and return the index of the pivot element
        def partition(arr, low, high):
            pivot = arr[high]  # Pivot is the last element
            i = low - 1 
            for j in range(low, high):
                # If the current element is smaller than or equal to the pivot
                if compareforheap(arr[j], pivot):
                    i += 1  # Increment index of the smaller element
                    arr[i], arr[j] = arr[j], arr[i]  # Swap

            # Swap the pivot element with the element at i+1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        # Main function to perform quick sort recursively
        def quick_sort_recursive(arr, low, high):
            if low < high:
                # Partition the array and get the pivot index
                pi = partition(arr, low, high)
                quick_sort_recursive(arr, low, pi - 1)
                quick_sort_recursive(arr, pi + 1, high)
        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]

        if valid_values:
            # Extract only the values for sorting
            array_to_sort = [value[0] for value in valid_values]
            quick_sort_recursive(array_to_sort, 0, len(array_to_sort) - 1)
            sorted_array = sorted(valid_values, key=lambda x: x[0])
            formatted_sorted_prices = [item[1] for item in sorted_array]

            for index, invalid in invalid_values_with_index:
                formatted_sorted_prices.insert(index, invalid)
            return column, formatted_sorted_prices 
        else:
            return [item[1] for item in invalid_values_with_index]

def counting_sort(data, column):
        print(f"Counting Sort is running on column: {column}")

        # Clean and extract data from the specified column
        cleaned_array = clean_data(data,column)
        valid_values = [item for item in cleaned_array if item[0] is not None]
        invalid_values = [item for item in cleaned_array if item[0] is None]

        if valid_values:
            max_val = max(item[0] for item in valid_values)
            min_val = min(item[0] for item in valid_values)

            range_val = int(max_val - min_val) + 1
            count = [0] * range_val
            output = [None] * len(valid_values)

            for item in valid_values:
                index = int(item[0] - min_val)  # Adjust index for counting
                count[index] += 1
            for i in range(1, range_val):
                count[i] += count[i - 1]

            # Build the output array
            for item in reversed(valid_values):
                index = int(item[0] - min_val)
                output[count[index] - 1] = item
                count[index] -= 1
            sorted_array = [item[1] for item in output] + [item[1] for item in invalid_values]
        else:
            sorted_array = [item[1] for item in invalid_values]
        return column, sorted_array 



def radix_sort(data, column):
        print(f"Radix Sort is running on column: {column}")

        # Clean and extract data from the specified column
        cleaned_array = clean_data(data,column)
        valid_values = [item for item in cleaned_array if item[0] is not None]
        invalid_values = [item for item in cleaned_array if item[0] is None]

        if valid_values:
            # Extract the numerical values for sorting and the original entries
            array = [float(item[0]) for item in valid_values]
            max_value = max(array)

            def counting_sort_for_radix(array, exp):
                n = len(array)
                output = [0] * n
                count = [0] * 10

                for i in range(n):
                    index = int(array[i]) // exp
                    count[index % 10] += 1
                
                for i in range(1, 10):
                    count[i] += count[i - 1]

                for i in range(n - 1, -1, -1):
                    index = int(array[i]) // exp
                    output[count[index % 10] - 1] = array[i]
                    count[index % 10] -= 1

                for i in range(n):
                    array[i] = output[i]
            exp = 1
            while max_value // exp > 0:
                counting_sort_for_radix(array, exp)
                exp *= 10
            sorted_valid_values = sorted(valid_values, key=lambda x: float(x[0]))
            sorted_array = [item[1] for item in sorted_valid_values] + [item[1] for item in invalid_values]
            data[column] = sorted_array
        else:
            # If no valid values, keep invalid entries in the original order
            data[column] = [item[1] for item in invalid_values]
        return column, sorted_array 
def bucket_sort(data, column):
        print(f"Bucket Sort is running on column: {column}")
        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values = [item[1] for item in cleaned_array if item[0] is None]

        if valid_values:
            # If there are valid values, proceed with bucket sort
            max_value = max(item[0] for item in valid_values)
            min_value = min(item[0] for item in valid_values)
            range_value = max_value - min_value
            bucket_count = 10  # Adjust this number based on your requirements
            buckets = [[] for _ in range(bucket_count)]
            for value, original in valid_values:
                if range_value == 0:  # All values are the same
                    index = 0
                else:
                    index = min(int((value - min_value) / (range_value / bucket_count)), bucket_count - 1)

                buckets[index].append((value, original)) 
            sorted_array = []
            for bucket in buckets:
                sorted_bucket = sorted(bucket, key=lambda x: x[0])
                sorted_array.extend(sorted_bucket)
            sorted_array = [item[1] for item in sorted_array]  
            sorted_array += invalid_values
            data[column] = sorted_array
        else:
            data[column] = invalid_values

        return column, sorted_array

def heap_sort(data, column):
        print(f"Heap Sort is running on column: {column}")
        def heapify(arr, n, i):
            largest = i  # Initialize largest as root
            left = 2 * i + 1  # left = 2*i + 1
            right = 2 * i + 2  # right = 2*i + 2
            if left < n and compareforheap(arr[left], arr[largest]):
                largest = left
            if right < n and compareforheap(arr[right], arr[largest]):
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # Swap
                heapify(arr, n, largest)  
        def heap_sort_recursive(arr):
            n = len(arr)
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max) to the end
                heapify(arr, i, 0)  
        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]

        if valid_values:
            array_to_sort = [value[0] for value in valid_values]
            heap_sort_recursive(array_to_sort)
            sorted_array = sorted(valid_values, key=lambda x: x[0])
            formatted_sorted_prices = [item[1] for item in sorted_array]
            for index, invalid in invalid_values_with_index:
                formatted_sorted_prices.insert(index, invalid)
            return column, formatted_sorted_prices 
        else:
            return [item[1] for item in invalid_values_with_index]
def compareforheap(a, b):
        # Comparison for ascending order
        if isinstance(a, str) and isinstance(b, str):
            return a.lower() > b.lower()  # For strings, return True if a is greater (to maintain max heap)
        return a > b  
def cocktail_shaker_sort(data, column):
        print(f"Cocktail Shaker Sort is running on column: {column}")
        def cocktail_shaker_sort_recursive(arr):
            n = len(arr)
            start = 0
            end = n - 1
            swapped = True

            while swapped:
                swapped = False
                # Forward pass
                for i in range(start, end):
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap the elements
                        swapped = True
                end -= 1
                if not swapped:
                    break
                swapped = False
                # Backward pass
                for i in range(end, start, -1):
                    if arr[i] < arr[i - 1]:
                        arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Swap the elements
                        swapped = True
                start += 1
        cleaned_array = clean_data(data,column)
        valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
        invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]
        if valid_values:
            # Extract only the values for sorting
            array_to_sort = [value[0] for value in valid_values]
            cocktail_shaker_sort_recursive(array_to_sort)
            sorted_array = sorted(valid_values, key=lambda x: x[0])
            formatted_sorted_prices = [item[1] for item in sorted_array]
            for index, invalid in invalid_values_with_index:
                formatted_sorted_prices.insert(index, invalid)
            return column, formatted_sorted_prices 
        else:
            return [item[1] for item in invalid_values_with_index]
def compare(a, b):
        if isinstance(a, str) and isinstance(b, str):
            return a.lower() < b.lower()
        return a < b
def shell_sort(data, column):
    print(f"Shell Sort is running on column: {column}")
    
    def shell_sort_recursive(arr):
        n = len(arr)
        gap = n // 2  
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                # Shift elements that are greater than temp to the right
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp  # Place temp at the correct position
            gap //= 2  

    cleaned_array = clean_data(data, column)  # Pass the data and column
    valid_values = [(item[0], item[1]) for item in cleaned_array if item[0] is not None]
    invalid_values_with_index = [(index, item[1]) for index, item in enumerate(cleaned_array) if item[0] is None]

    if valid_values:
        # Extract only the values for sorting
        array_to_sort = [value[0] for value in valid_values]
        shell_sort_recursive(array_to_sort)
        sorted_array = sorted(valid_values, key=lambda x: x[0])
        formatted_sorted_prices = [item[1] for item in sorted_array]

        for index, invalid in invalid_values_with_index:
            formatted_sorted_prices.insert(index, invalid)

        return column, formatted_sorted_prices 
    else:
        return [item[1] for item in invalid_values_with_index]
def clean_data(data, column):
    """Clean and extract values from column data based on the type of column."""

    def clean_price_or_shipping(value):
        """Extract numeric values for Price or Shipping Cost."""
        if not value or "not found" in value.lower() or "not specified" in value.lower() or "free" in value.lower():
            return None
        range_match = re.search(r'\$?(\d+(?:,\d{3})*\.\d{2})\s+to\s+\$?(\d+(?:,\d{3})*\.\d{2})', value)
        if range_match:
            # Extract the minimum value from the range
            return float(range_match.group(1).replace(',', ''))
        match = re.search(r'\$?(\d+(?:,\d{3})*\.\d{2})', value)
        if match:
            return float(match.group(1).replace(',', ''))
        return None

    def extract_percentage(seller):
        """Extract percentage from Seller Info."""
        match = re.search(r'(\d{1,3}\.\d)%', seller)
        return float(match.group(1)) if match else None

    def extract_quantity(sold_entry):
        """Extract the quantity sold."""
        if "not found" in sold_entry.lower():
            return None
        match = re.search(r'(\d{1,3}(?:,\d{3})*)\+?', sold_entry)
        return int(match.group(1).replace(',', '')) if match else None

    def extract_country(location):
        """Extract country from Location."""
        match = re.search(r'from\s+(.+)', location)
        return match.group(1).strip().lower() if match else ''

    def normalize_name(name):
        """Normalize the Phone Name or Condition for sorting."""
        return name.strip().lower()

    if column in ["Price", "Shipping Cost"]:
        cleaned_array = [(clean_price_or_shipping(val), val) for val in data[column].tolist()]
    elif column == "Seller Info":
        cleaned_array = [(extract_percentage(val), val) for val in data[column].tolist()]
    elif column == "Quantity Sold":
        cleaned_array = [(extract_quantity(val), val) for val in data[column].tolist()]
    elif column == "Location":
        cleaned_array = [(extract_country(val), val) for val in data[column].tolist()]
    elif column in ["Phone Name", "Condition"]:
        cleaned_array = [(normalize_name(val), val) for val in data[column].tolist()]
    else:
        cleaned_array = [(None, val) for val in data[column].tolist()]

    return cleaned_array


