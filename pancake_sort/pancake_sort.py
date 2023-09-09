def flipfront(lst: list, n: int) -> list:
    return lst[n-1::-1] + lst[n:]

def flipfront_in_place(lst: list, n: int):
    lst[:n] = lst[n-1::-1]
    
def max_value_index(lst: list):
    max_index = len(lst) - 1
    max_val = lst[max_index]
    for i in range(max_index)[::-1]:
        if max_val < lst[i]:
            max_val = lst[i]
            max_index = i
    return max_index

def pancake_sort(lst: list):
    for x in range(1, len(lst) + 1)[::-1]:
        y = max_value_index(lst[:x]) + 1
        if y < x:
            flipfront_in_place(lst, y) 
            flipfront_in_place(lst, x)
            
def main():
    mylist = [15, 9, 2, 4, 1, 0, -1, 78, 22, 67, 83, -22, 54, 17]
    pancake_sort(mylist)
    print(mylist)
            
if __name__ == "__main__":
    main()