# python3


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2,-1,-1):
        swaps = shift_down(data, swaps, i)
    return swaps


def shift_down(data, swaps, i):
    n=len(data)
    min_index=i
    left =2*i+1
    if left < n and data[left]<data[min_index]:
        min_index=left
    right= 2*i+2
    if right < n and data[right]<data[min_index]:
        min_index = right
    if i !=min_index:
        data[i], data[min_index]=data[min_index], data[i]
        swaps.append((i,min_index))
        swaps = shift_down(data, swaps, min_index)
    return swaps

def main():
    
    input_method = input()
    if "I" in input_method:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_method:
        file = input().strip()
        path= "./test/"+file
        with open(path, 'r', encoding='utf-8') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    assert len(data) == n
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
