# --------------------------------------MERGESORT-----------------------------------------
statics=[]
def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        leftside = nums[:mid]
        rightside = nums[mid:]

        mergeSort(leftside)
        mergeSort(rightside)

        i = 0
        j = 0
        k = 0
        while i < len(leftside) and j < len(rightside):
            if leftside[i] < rightside[j]:
                nums[k] = leftside[i]
                i = i + 1
            else:
                nums[k] = rightside[j]
                j = j + 1
            k = k + 1

        while i < len(leftside):
            nums[k] = leftside[i]
            i = i + 1
            k = k + 1

        while j < len(rightside):
            nums[k] = rightside[j]
            j = j + 1
            k = k + 1


# ----------------------------------------QUICKSORT----------------------------------------
def quickSort(nums):
    quickSortHelper(nums, 0, len(nums) - 1)


def quickSortHelper(nums, first, last):
    if first < last:
        splitpoint = partition(nums, first, last)

        quickSortHelper(nums, first, splitpoint - 1)
        quickSortHelper(nums, splitpoint + 1, last)


def partition(nums, first, last):
    pivotvalue = nums[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and nums[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while nums[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = nums[leftmark]
            nums[leftmark] = nums[rightmark]
            nums[rightmark] = temp

    temp = nums[first]
    nums[first] = nums[rightmark]
    nums[rightmark] = temp

    return rightmark


# -------------------------------BINARYSEARCH-----------------------------------------------

def binarySearch(nums, ari):
    flag=0
    sum=0
    count=0
    global statics
    while len(nums) >= 2 and flag==0:

        mid = len(nums) // 2
        sum += 1

        if nums[mid] == ari:
            flag = 1
        elif nums[mid] > ari:
            nums = nums[:mid]
        else:
            nums = nums[mid:]
    statics.append(sum)


    return flag


# ---------------------------------interpolation search---------------------------------------------

def interpolationSearch(nums, len, ari):
    lo = 0
    hi = (len - 1)


    while lo <= hi and ari >= nums[lo] and ari <= nums[hi]:

                pos = lo + int(((float(hi - lo) /
                         (nums[hi] - nums[lo])) * (ari - nums[lo])))


                if nums[pos] == ari:
                    return 1

                elif nums[pos] < ari:

                    lo = pos + 1

                else:
                    hi = pos - 1

    return -1


f = input("φορτωσε το αρχειο που θες\n")

nums = []

with open(f, "r") as file:
    nums = [int(line.strip()) for line in file]

answer = input("1: ταξινομιση με mergeshort\n2: ταξινομιση με quicksort\n")

if answer == "1":

    mergeSort(nums)
    print(nums)
    ar = input("δωσε εναν αριθμο για αναζητηση:\n")
    while ar != "q":
        ari = int(ar)
        answ = input("1:binary search\n2:interpolation search\n")
        if answ == "1":
            exist = binarySearch(nums, ari)
            if exist is 1:
                print("found")
            else:
                print("den found")
        else:
            exist = interpolationSearch(nums,len(nums),ari)
            if exist is 1:
                print("found")
            else:
                print("den found")

        ar = input("δωσε εναν αριθμο για αναζητηση:\n")
    print(statics)
else:

    quickSort(nums)
    print(nums)
    ar = input("δωσε εναν αριθμο για αναζητηση:\n")
    while ar != "q":
        ari = int(ar)
        answ = input("1:binary search\n2:interpolation search\n")
        if answ == "1":
            exists = binarySearch(nums, ari)
            if exists is 1:
                print("found")
            else:
                print("do not found")
        else:
            exist = interpolationSearch(ari)
            if exist is 1:
                print("found")
            else:
                print("do not found")

        ar = input("δωσε εναν αριθμο για αναζητηση:\n")

    print(statics)