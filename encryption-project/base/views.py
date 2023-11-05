from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    context = {}
    return render(request, 'base/home.html', context)


def prepare_matrix(key):
    matrix = [[],
              [],
              [],
              [],
              []]

    modified_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i/j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u',
                         'v', 'w', 'x', 'y', 'z']

    duplicates = []
    key = list(key)

    table = 0
    for item in key:
        if item == 'i' or item == 'j':
            item = 'i/j'
        if item in duplicates:
            continue
        if len(matrix[table]) == 5:
            table += 1
        matrix[table].append(item)
        modified_alphabet.remove(item)
        if item not in duplicates:
            duplicates.append(item)

    for item in modified_alphabet:
        if len((matrix[table])) == 5:
            table += 1
        matrix[table].append(item)

    return matrix


def playfair_encryption(request):
    if request.method == 'POST':
        key = request.POST.get('encryption_key')
        message = request.POST.get('encryption_message')

        matrix = prepare_matrix(key)
        pairs = [message[i:i + 2] for i in range(0, len(message), 2)]
        result = ''
        for item in pairs:
            first_index, second_index = -1, -2
            first, second = list(item)
            if first == 'i' or first == 'j':
                first = 'i/j'
            if second == 'i' or second == 'j':
                second = 'i/j'
            # First Example
            for table in matrix:
                if first in table and second in table:
                    if table.index(first) == 4:
                        result += table[0] + table[table.index(second) + 1]
                    elif table.index(second) == 4:
                        result += table[table.index(first) + 1] + table[0]
                    else:
                        result += table[table.index(first) + 1] + table[table.index(second) + 1]
                    break

                # Second Example
                if first in table:
                    first_index, first_table = table.index(first), table
                if second in table:
                    second_index, second_table = table.index(second), table
                if first_index == second_index:
                    first_table_index = matrix.index(first_table)
                    second_table_index = matrix.index(second_table)
                    if first_table_index == 4:
                        first_table_index = -1
                    if second_table_index == 4:
                        second_table_index = -1
                    result += matrix[first_table_index + 1][second_index] + matrix[second_table_index + 1][
                        first_index]
                    break

            # Third case
            else:
                result += first_table[second_index] + second_table[first_index]

        context = {'result': result}
        return JsonResponse(context)

    return render(request, 'base/playfair.html')


def playfair_decryption(request):
    if request.method == 'POST':
        key = request.POST.get('decryption_key')
        message = request.POST.get('decryption_message')

        matrix = prepare_matrix(key)
        pairs = [message[i:i + 2] for i in range(0, len(message), 2)]
        result = ''
        for item in pairs:
            first_index, second_index = -1, -2
            first, second = list(item)
            if first == 'i' or first == 'j':
                first = 'i/j'
            if second == 'i' or second == 'j':
                second = 'i/j'
            # First Example
            for table in matrix:
                if first in table and second in table:
                    if table.index(first) == 0:
                        result += table[4] + table[table.index(second) - 1]
                    elif table.index(second) == 0:
                        result += table[table.index(first) - 1] + table[4]
                    else:
                        result += table[table.index(first) - 1] + table[table.index(second) - 1]
                    break

                # Second Example
                if first in table:
                    first_index, first_table = table.index(first), table
                if second in table:
                    second_index, second_table = table.index(second), table
                if first_index == second_index:
                    first_table_index = matrix.index(first_table)
                    second_table_index = matrix.index(second_table)
                    if first_table_index == 0:
                        first_table_index = 5
                    if second_table_index == 0:
                        second_table_index = 5
                    result += matrix[first_table_index - 1][second_index] + matrix[second_table_index - 1][
                        first_index]
                    break

            # Third case
            else:
                result += first_table[second_index] + second_table[first_index]

        context = {'result': result}
        return JsonResponse(context)

    return render(request, 'base/playfair.html')