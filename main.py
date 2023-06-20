from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    data = get_data()
    data = get_filtered_data(data)
    data = get_last_values(data, 5)
    data = get_formatted_data(data)

    for operation in data:
        print(operation)


if __name__ == '__main__':
    main()
