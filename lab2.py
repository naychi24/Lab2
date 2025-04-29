def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    str_list = user_input.split(",")
    float_list = [float(num.strip()) for num in str_list]
    return float_list

def calc_average(lst):
    return sum(lst) / len(lst) if lst else 0

def find_min_max(lst):
    return [min(lst), max(lst)] if lst else [None, None]

def sort_temperature(lst):
    return sorted(lst)

def calc_median_temperature(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n == 0:
        return None
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Average Temperature:", calc_average(num_list))
    print("Min and Max Temperature:", find_min_max(num_list))
    print("Sorted Temperature List:", sort_temperature(num_list))
    print("Median Temperature:", calc_median_temperature(num_list))

if __name__ == "__main__":
    main()