# Historical data as a list
historical_data = [55, 49, 34, 46, 29, 2, 15, 3, 8, 16, 10, 36, 47, 59, 37, 31, 50, 44, 28, 11, 46, 1, 24, 18, 9, 26]

# Function to predict the next numbers based on consecutive sequences
def predict_next_numbers(data, n=5):
    predictions = []
    max_sequence_length = 5  # Adjust this based on the maximum sequence length you want to consider
    
    # Create a dictionary to count consecutive sequences
    sequence_counts = {}
    current_sequence = []

    for num in data:
        if len(current_sequence) == max_sequence_length:
            sequence = tuple(current_sequence)
            if sequence not in sequence_counts:
                sequence_counts[sequence] = 1
            else:
                sequence_counts[sequence] += 1
            current_sequence.pop(0)

        current_sequence.append(num)

    # Find the most common sequence
    most_common_sequence = max(sequence_counts, key=sequence_counts.get)

    # Predict the next numbers based on the most common sequence
    for _ in range(n):
        next_num = most_common_sequence[0]
        predictions.append(next_num)
        most_common_sequence = most_common_sequence[1:] + (next_num,)

    return predictions

# Predict the next 5 numbers
next_numbers = predict_next_numbers(historical_data, n=5)
print("Predicted next numbers based on consecutive sequences:", next_numbers)