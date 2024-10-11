import pandas as pd
import re

def multiheap_sort(data, column1, column2):
        print(f"Heap Sort is running on columns: {column1} and {column2}")
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and compare_for_heap(arr[left][0], arr[largest][0]) and arr[left][1] == arr[largest][1]:
                largest = left
            elif left < n and arr[left][0] == arr[largest][0] and compare_for_heap(arr[left][1], arr[largest][1]):
                largest = left
            if right < n and compare_for_heap(arr[right][0], arr[largest][0]) and arr[right][1] == arr[largest][1]:
                largest = right
            elif right < n and arr[right][0] == arr[largest][0] and compare_for_heap(arr[right][1], arr[largest][1]):
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heap_sort_recursive(arr):
            n = len(arr)

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)

        multi_cleaned_array = multi_clean_data(data,column1, column2)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]

        if valid_values:
            heap_sort_recursive(valid_values)
            sorted_names_and_prices = valid_values
            for idx, (name, price) in zip(data.index, sorted_names_and_prices):
                data.loc[idx, column1] = name
                data.loc[idx, column2] = price    
        else:
            print("No valid values to sort.")
        
def compare_for_heap(a, b):
        """Compare two values for heap sorting."""
        if a is None and b is None:
            return False  # Both are equal
        elif a is None:
            return False  # Treat None as less than any number
        elif b is None:
            return True   # Treat any number as greater than None
        return a > b  
def get_value(item, column):
        """Safely extract the value of a specific column from an item."""
        if item is None or not isinstance(item, tuple):
            return None
        return item[column] if column in item else None

def multi_clean_data(data,column1, column2):
        """Clean and extract values from two columns of data based on their types."""

        def clean_price_or_shipping(value):
            """Extract numeric values for Price or Shipping Cost."""
            if isinstance(value, (int, float)):
                return value
            if not value or "not found" in value.lower() or "not specified" in value.lower() or "free" in value.lower():
                return None
            match = re.search(r'\$?(\d+(?:,\d{3})*\.\d{2})', value)
            if match:
                return float(match.group(1).replace(',', ''))
            # Handle ranges (e.g., $270.75 to $650.75)
            range_match = re.search(r'\$(\d+(?:,\d{3})*\.\d{2})\s+to\s+\$(\d+(?:,\d{3})*\.\d{2})', value)
            if range_match:
                return float(range_match.group(1).replace(',', ''))
            return None
        def extract_percentage(value):
            """Extract percentage from a string."""
            if not isinstance(value, str):
                return None
            match = re.search(r'(\d{1,3}\.\d)%', value)
            if match:
                return float(match.group(1))
            return None

        def extract_quantity(value):
            """Extract quantity sold from a string."""
            if isinstance(value, int):
                return value
            if not value or "not found" in value.lower() or "not specified" in value.lower():
                return None
            match = re.search(r'(\d+(?:,\d{3})*\+?)', value)
            if match:
                return int(match.group(1).replace(',', '').rstrip('+'))  # Remove the plus sign
            return None

        def extract_country(location):
            """Extract country from Location."""
            match = re.search(r'from\s+(.+)', location)
            return match.group(1).strip().lower() if match else ''

        def normalize_name(name):
            """Normalize the Phone Name or Condition for sorting."""
            return name.strip().lower()
        cleaned_column1 = []
        if column1 in ["Price", "Shipping Cost"]:
            cleaned_column1 = [clean_price_or_shipping(val) for val in data[column1].tolist()]
        elif column1 == "Seller Info":
            cleaned_column1 = [extract_percentage(val) for val in data[column1].tolist()]
        elif column1 == "Quantity Sold":
            cleaned_column1 = [extract_quantity(val) for val in data[column1].tolist()]
        elif column1 == "Location":
            cleaned_column1 = [extract_country(val) for val in data[column1].tolist()]
        elif column1 in ["Phone Name", "Condition"]:
            cleaned_column1 = [normalize_name(val) for val in data[column1].tolist()]
        else:
            cleaned_column1 = [None for val in data[column1].tolist()]
        cleaned_column2 = []
        if column2 in ["Price", "Shipping Cost"]:
            cleaned_column2 = [clean_price_or_shipping(val) for val in data[column2].tolist()]
        elif column2 == "Seller Info":
            cleaned_column2 = [extract_percentage(val) for val in data[column2].tolist()]
        elif column2 == "Quantity Sold":
            cleaned_column2 = [extract_quantity(val) for val in data[column2].tolist()]
        elif column2 == "Location":
            cleaned_column2 = [extract_country(val) for val in data[column2].tolist()]
        elif column2 in ["Phone Name", "Condition"]:
            cleaned_column2 = [normalize_name(val) for val in data[column2].tolist()]
        else:
            cleaned_column2 = [None for val in data[column2].tolist()]

        # Combine cleaned data for both columns, keeping the original values
        cleaned_array = []
        for i in range(len(cleaned_column1)):
            cleaned_array.append((cleaned_column1[i], cleaned_column2[i], data[column1].iloc[i], data[column2].iloc[i]))

        return cleaned_array



def multi_bubble_sort(data, column1, column2):
        print(f"Bubble Sort is running on columns: {column1} and {column2}")

        multi_cleaned_array = multi_clean_data(data,column1, column2)

        # Create a list of tuples (col1_value, col2_value)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]

        if valid_values:
            n = len(valid_values)

            # Bubble sort algorithm for multicolumn sorting
            for i in range(n):
                for j in range(0, n - i - 1):
                    # Compare the primary column first
                    if (valid_values[j][0] > valid_values[j + 1][0]) or (
                        valid_values[j][0] == valid_values[j + 1][0] and valid_values[j][1] > valid_values[j + 1][1]):
                        # Swap if the current element is greater than the next element
                        valid_values[j], valid_values[j + 1] = valid_values[j + 1], valid_values[j]

            # Extract sorted col1 and col2 values
            sorted_values = valid_values

            # Update original data with sorted values
            for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val
        
        else:
            print("No valid values to sort.")
def multi_selection_sort(data, column1, column2):
        print(f"Selection Sort is running on columns: {column1} and {column2}")

        multi_cleaned_array = multi_clean_data(data,column1, column2)

        # Create a list of tuples (col1_value, col2_value)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]

        if valid_values:
            n = len(valid_values)
            for i in range(n):
                min_index = i
                for j in range(i + 1, n):
                    # Compare the primary column first
                    if (valid_values[j][0] < valid_values[min_index][0]) or (
                        valid_values[j][0] == valid_values[min_index][0] and valid_values[j][1] < valid_values[min_index][1]):
                        min_index = j
                valid_values[i], valid_values[min_index] = valid_values[min_index], valid_values[i]
            sorted_values = valid_values
            for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val

        
        else:
            print("No valid values to sort.")
def multi_insertion_sort(data, column1, column2):
        print(f"Insertion Sort is running on columns: {column1} and {column2}")
        multi_cleaned_array = multi_clean_data(data,column1, column2)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]
        if valid_values:
            for i in range(1, len(valid_values)):
                key = valid_values[i]
                j = i - 1
                while j >= 0 and ((valid_values[j][0] > key[0]) or 
                                (valid_values[j][0] == key[0] and valid_values[j][1] > key[1])):
                    valid_values[j + 1] = valid_values[j]
                    j -= 1
                valid_values[j + 1] = key
            sorted_values = valid_values
            for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val

        else:
            print("No valid values to sort.")
def multi_merge_sort(data, column1, column2):
            print(f"Merge Sort is running on columns: {column1} and {column2}")
            multi_cleaned_array = multi_clean_data(data,column1, column2)
            valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]

            if valid_values:
                # Merge Sort algorithm for multicolumn sorting
                def merge_sort(arr):
                    if len(arr) > 1:
                        mid = len(arr) // 2  # Finding the mid of the array
                        left_half = arr[:mid]  # Dividing the array elements into 2 halves
                        right_half = arr[mid:]
                        merge_sort(left_half)  # Sorting the first half
                        merge_sort(right_half)  # Sorting the second half
                        i = j = k = 0
                        while i < len(left_half) and j < len(right_half):
                            if (left_half[i][0] < right_half[j][0]) or (
                                left_half[i][0] == right_half[j][0] and left_half[i][1] < right_half[j][1]):
                                arr[k] = left_half[i]
                                i += 1
                            else:
                                arr[k] = right_half[j]
                                j += 1
                            k += 1

                        # Checking if any element was left
                        while i < len(left_half):
                            arr[k] = left_half[i]
                            i += 1
                            k += 1

                        while j < len(right_half):
                            arr[k] = right_half[j]
                            j += 1
                            k += 1
                merge_sort(valid_values)
                sorted_values = valid_values
                for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                    data.loc[idx, column1] = col1_val
                    data.loc[idx, column2] = col2_val

            else:
                print("No valid values to sort.")

def multi_quick_sort(data, column1, column2):
        print(f"Quick Sort is running on columns: {column1} and {column2}")

        multi_cleaned_array = multi_clean_data(data,column1, column2)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]
        if valid_values:
            def quick_sort(arr, low, high):
                if low < high:
                    pi = partition(arr, low, high)
                    quick_sort(arr, low, pi - 1)
                    quick_sort(arr, pi + 1, high)

            def partition(arr, low, high):
                # Choose the rightmost element as pivot
                pivot = arr[high]
                i = low - 1
                for j in range(low, high):
                    # Compare using the first and second column for sorting
                    if (arr[j][0] < pivot[0]) or (arr[j][0] == pivot[0] and arr[j][1] < pivot[1]):
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]  # Swap

                arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to the correct position
                return i + 1

            # Sort using quick sort
            quick_sort(valid_values, 0, len(valid_values) - 1)

            # Update original data with sorted values
            for idx, (col1_val, col2_val) in zip(data.index,  valid_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val

        else:
            print("No valid values to sort.")
def multi_counting_sort(data, column1, column2):
        print(f"Counting Sort is running on columns: {column1} and {column2}")

        multi_cleaned_array = multi_clean_data(data,column1, column2)

        # Create a list of tuples (col1_value, col2_value) with valid entries
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]

        if valid_values:
            # Determine the range of column1 values
            max_col1 = max(item[0] for item in valid_values)
            min_col1 = min(item[0] for item in valid_values)

            # If dealing with floats, convert to integers
            if isinstance(max_col1, float) or isinstance(min_col1, float):
                factor = 100  # Example: scale by 100
                max_col1 = int(max_col1 * factor)
                min_col1 = int(min_col1 * factor)
            else:
                factor = 1  
            range_of_elements = max_col1 - min_col1 + 1
            count = [0] * range_of_elements
            output = [None] * len(valid_values)

            # Store the count of each element in count[]
            for item in valid_values:
                index = int(item[0] * factor) - min_col1
                count[index] += 1
            for i in range(1, len(count)):
                count[i] += count[i - 1]
            for item in reversed(valid_values):
                index = int(item[0] * factor) - min_col1
                output[count[index] - 1] = item
                count[index] -= 1
            sorted_values = []
            current_col1_value = None
            temp_col2_values = []

            for item in output:
                if current_col1_value is None or item[0] != current_col1_value:
                    if temp_col2_values:
                        temp_col2_values.sort(key=lambda x: x[1])  # Sorting by column2 value (ascending)
                        sorted_values.extend(temp_col2_values)

                    current_col1_value = item[0]
                    temp_col2_values = [item]
                else:
                    temp_col2_values.append(item)

            # Sort any remaining items in temp_col2_values
            if temp_col2_values:
                temp_col2_values.sort(key=lambda x: x[1])  # Sort remaining by column2
                sorted_values.extend(temp_col2_values)

            # Update original data with sorted values
            for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val

        else:
            print("No valid values to sort.")
def multi_radix_sort(data, col_1, col_2):
        print(f"Radix Sort is running on columns: {col_1} and {col_2}")

        multi_cleaned_array = multi_clean_data(data,col_1, col_2)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]

        if valid_values:
            
                numeric_values = [int(item[0]) for item in valid_values]
                def counting_sort(arr, exp):
                    n = len(arr)
                    output = [0] * n
                    count = [0] * 10
                    for i in range(n):
                        index = arr[i] // exp
                        count[index % 10] += 1
                    for i in range(1, 10):
                        count[i] += count[i - 1]
                    for i in range(n - 1, -1, -1):
                        index = arr[i] // exp
                        output[count[index % 10] - 1] = arr[i]
                        count[index % 10] -= 1
                    for i in range(n):
                        arr[i] = output[i]
                def radix_sort(arr):
                    # Find the maximum number to know the number of digits
                    max_value = max(arr)
                    exp = 1

                    # Do counting sort for every digit
                    while max_value // exp > 0:
                        counting_sort(arr, exp)
                        exp *= 10
                radix_sort(numeric_values)
                sorted_values = [(str(num), next(item[1] for item in valid_values if int(item[0]) == num)) for num in numeric_values]
                for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                    data.loc[idx, col_1] = col1_val
                    data.loc[idx, col_2] = col2_val
                
            # except ValueError as e:
            #     # Handle case where conversion to int fails
            #     show_error_message(f"Error: {e} - Please ensure the data in {col_1} is numeric.")
            # except TypeError as e:
            #     # Handle case where an operation fails due to incorrect types
            #     self.show_error_message(f"Error: {e} - Please ensure the data in {col_1} is numeric.")
        else:
            print("No valid values to sort.")
def multi_bucket_sort(data, column1, column2):
        print(f"Bucket Sort is running on columns: {column1} and {column2}")

        multi_cleaned_array = multi_clean_data(data,column1, column2)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]

        if valid_values:
            def bucket_sort(arr):
                # Create buckets
                buckets = {}
                for item in arr:
                    key = item[0]  # Use column1 value as the bucket key
                    if key not in buckets:
                        buckets[key] = []
                    buckets[key].append(item)
                sorted_values = []
                for key in sorted(buckets.keys()):  # Sort keys to maintain order
                    # Sort bucket by column2 value using insertion sort
                    bucket = buckets[key]
                    for i in range(1, len(bucket)):
                        key_item = bucket[i]
                        j = i - 1
                        while j >= 0 and bucket[j][1] > key_item[1]:
                            bucket[j + 1] = bucket[j]
                            j -= 1
                        bucket[j + 1] = key_item
                    sorted_values.extend(bucket)
                return sorted_values
            sorted_values = bucket_sort(valid_values)
            for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val

    
        else:
            print("No valid values to sort.")
def multi_shell_sort(data, column1, column2):
        print(f"Shell Sort is running on columns: {column1} and {column2}")

        multi_cleaned_array = multi_clean_data(data,column1, column2)

        # Create a list of tuples (col1_value, col2_value)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]
        if valid_values:
            # Shell Sort algorithm for multicolumn sorting
            def shell_sort(arr):
                n = len(arr)
                gap = n // 2
                while gap > 0:
                    for i in range(gap, n):
                        temp = arr[i]
                        j = i
                        # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
                        while j >= gap and ((arr[j - gap][0] > temp[0]) or 
                                            (arr[j - gap][0] == temp[0] and arr[j - gap][1] > temp[1])):
                            arr[j] = arr[j - gap]
                            j -= gap
                        arr[j] = temp
                    gap //= 2  
            shell_sort(valid_values)
            sorted_values = valid_values
            for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val


        else:
            print("No valid values to sort.")
def multi_cocktail_shaker_sort(data, column1, column2):
        print(f"Cocktail Shaker Sort is running on columns: {column1} and {column2}")

        multi_cleaned_array = multi_clean_data(data,column1, column2)
        valid_values = [(item[0], item[1]) for item in multi_cleaned_array if item[0] is not None and item[1] is not None]
        if valid_values:
            def cocktail_shaker_sort(arr):
                n = len(arr)
                swapped = True
                start = 0
                end = n - 1
                
                while swapped:
                    swapped = False
                    
                    for i in range(start, end):
                        if (arr[i][0] > arr[i + 1][0]) or (arr[i][0] == arr[i + 1][0] and arr[i][1] > arr[i + 1][1]):
                            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap
                            swapped = True
                            
                    end -= 1
                    for i in range(end, start, -1):
                        if (arr[i][0] < arr[i - 1][0]) or (arr[i][0] == arr[i - 1][0] and arr[i][1] < arr[i - 1][1]):
                            arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Swap
                            swapped = True                            
                    start += 1
            cocktail_shaker_sort(valid_values)
            sorted_values = valid_values
            for idx, (col1_val, col2_val) in zip(data.index, sorted_values):
                data.loc[idx, column1] = col1_val
                data.loc[idx, column2] = col2_val

    
        else:
            print("No valid values to sort.")
