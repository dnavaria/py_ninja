from generate_data import generate_num_list
from generate_data import choose_input
from generate_data import remove_dups

def binary_search(data: list, query: int) -> bool:
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((low+high)/2)
        print(f"low :: {low}, high :: {high}, mid :: {mid}")
        if data[mid] == query:
            return True
        elif data[mid] > query:
            high = mid - 1
        elif data[mid] < query:
            low = mid + 1
    return False


if __name__ == '__main__':
    data = generate_num_list(length=10)
    ip = choose_input(data=data)
    data = remove_dups(data)
    data.sort()
    print(f"data :: {data}")
    print(f"input :: {ip}")
    print(f"result :: {binary_search(data, ip)}")
