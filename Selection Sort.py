class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            cur_min = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[cur_min]:
                    cur_min = j
            arr[i], arr[cur_min] = arr[cur_min], arr[i]
